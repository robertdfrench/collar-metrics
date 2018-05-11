import os
import boto3
from boto3.dynamodb.conditions import Key


def endpoint():
    return os.environ.get('DYNAMODB_ENDPOINT')


class BarksTable(object):
    def __init__(self):
        self.barks = []
        self.dynamodb = boto3.client('dynamodb', endpoint_url=endpoint())
        self.table_name = 'collar-metrics-barks'

    def gracefully_create_table(self):
        if not self._table_exists():
            self._create_table()

    def _table_exists(self):
        table_names = self.dynamodb.list_tables()['TableNames']
        return self.table_name in table_names

    def _create_table(self):
        self.dynamodb.create_table(
            TableName=self.table_name,
            AttributeDefinitions=[
                {"AttributeName": "collarid", "AttributeType": "S"},
                {"AttributeName": "timestamp", "AttributeType": "S"}
            ],
            KeySchema=[
                {"AttributeName": "collarid", "KeyType": "HASH"},
                {"AttributeName": "timestamp", "KeyType": "RANGE"},
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

    def by_collar(self, collar_id):
        bark_records = self.dynamodb.query(
            TableName=self.table_name,
            KeyConditionExpression="collarid = :collar",
            ExpressionAttributeValues={":collar": {"S": collar_id}}
        )['Items']
        return [format_for_api(x) for x in bark_records]

    def add(self, **kwargs):
        self.dynamodb.put_item(
            TableName=self.table_name,
            Item={
                "collarid": {"S": kwargs['collar']},
                "volume": {"N": str(kwargs['volume'])},
                "timestamp": {"S": kwargs['timestamp']}
            }
        )


def format_for_api(bark_record):
    return {
        "type": "barks",
        "attributes": {
            "volume": bark_record['volume']['N'],
            "timestamp": bark_record['timestamp']['S']
        }
    }
