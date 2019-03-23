import logging
from typing import Dict, List

logger = logging.getLogger('Condition')
logger.setLevel(logging.INFO)


class Condition():
    SCORE_THRESHOLD = 0.5

    def __init__(self, entities: List[Dict]):
        self.__entities = entities
        self.__organs = None
        self.__symptoms = None

    def __parse(self):
        # Doc: https://docs.aws.amazon.com/comprehend/latest/dg/API_hera_Entity.html
        self.__organs = []
        self.__symptoms = []

        for entity in self.__entities:
            if not self.__is_trustable(entity):
                logger.debug('Score too low. Ignore entity %s', entity)
                continue

            if 'Type' in entity and entity['Type'] == 'SYSTEM_ORGAN_SITE':
                self.__organs.append(entity['Text'])

            if 'Traits' in entity:
                for trait in entity['Traits']:
                    if self.__is_trustable(trait):
                        self.__symptoms.append(trait['Name'])

    def __is_trustable(self, entity: Dict):
        return 'Score' not in entity or entity['Score'] > self.SCORE_THRESHOLD

    @property
    def organs(self):
        if not self.__organs:
            self.__parse()
        return self.__organs

    @property
    def symptoms(self):
        if not self.__symptoms:
            self.__parse()
        return self.__symptoms
