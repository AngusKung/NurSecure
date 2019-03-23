from pprint import pprint

import boto3


# Doc: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html
session = boto3.Session(profile_name='nursecure')
client = session.client(service_name='comprehendmedical')
result = client.detect_entities(Text= 'cerealx 84 mg daily')
entities = result['Entities']
for entity in entities:
    pprint(entity)