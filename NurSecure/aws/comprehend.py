import logging

import boto3

from .condition import Condition

logger = logging.getLogger('Comprehend')
logger.setLevel(logging.INFO)


class Comprehend():
    '''Doc: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html'''

    def __init__(self):
        session = boto3.Session(profile_name='nursecure')
        self.client = session.client(service_name='comprehendmedical')

    def query(self, text: str):
        result = self.client.detect_entities(Text=text)
        entities = result['Entities']
        logger.debug(entities)
        return Condition(entities)
