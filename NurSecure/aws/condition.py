import logging
from typing import Any, Dict, List, Set

logger = logging.getLogger('Condition')
logger.setLevel(logging.INFO)


class Condition():
    SCORE_THRESHOLD = 0.5

    def __init__(self, entities: List[Dict[str, Any]]):
        self.__entities = entities
        self.__organs = None
        self.__symptoms = None

    def __parse(self):
        # Doc: https://docs.aws.amazon.com/comprehend/latest/dg/API_hera_Entity.html
        self.__organs = set()
        self.__symptoms = set()

        for entity in self.__entities:
            if not self.__is_trustable(entity):
                logger.debug('Score too low. Ignore entity %s', entity)
                continue

            if 'Type' in entity and entity['Type'] == 'SYSTEM_ORGAN_SITE':
                self.__organs.add(entity['Text'])

            if 'Traits' in entity:
                for trait in entity['Traits']:
                    if not self.__is_trustable(trait):
                        continue
                    if 'Name' in trait and trait['Name'] == 'SYMPTOM':
                        self.__symptoms.add(entity['Text'])

    def __is_trustable(self, entity: Dict):
        return 'Score' not in entity or entity['Score'] > self.SCORE_THRESHOLD

    @property
    def organs(self) -> Set[str]:
        if self.__organs is None:
            self.__parse()
        return self.__organs

    @property
    def symptoms(self) -> Set[str]:
        if self.__symptoms is None:
            self.__parse()
        return self.__symptoms
