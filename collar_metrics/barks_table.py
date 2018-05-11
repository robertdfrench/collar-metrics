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
        return self.table_name in self.dynamodb.list_tables(
            ExclusiveStartTableName=self.table_name,
            Limit=1
        )['TableNames']

    def _create_table(self):
        self.dynamodb.create_table(
            TableName=self.table_name,
            AttributeDefinitions=[{"AttributeName": "collarid", "AttributeType": "S"}],
            KeySchema=[{"AttributeName": "collarid", "KeyType": "HASH"}],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

    @property
    def _table(self):
        return self.dynamodb.Table(self.table_name)

    def by_collar(self, collar_id):
        return self.dynamodb.query(
            TableName=self.table_name,
            KeyConditionExpression="collarid = :collar",
            ExpressionAttributeValues={":collar": {"S": collar_id}}
        )['Items']

    def add(self, **kwargs):
        self.dynamodb.put_item(
            TableName=self.table_name,
            Item={"collarid": {"S": kwargs['collar']}}
        )
