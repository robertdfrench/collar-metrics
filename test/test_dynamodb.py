import boto3
import pytest

@pytest.fixture
def client():
    return boto3.client('dynamodb',
        endpoint_url='http://localhost:8000',
        region_name='us-east-1'
    )


def test_can_create_table(client):
    client.create_table(
        TableName="collar-metrics-barks-test",
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
	ProvisionedThroughput={
	    'ReadCapacityUnits': 5,
	    'WriteCapacityUnits': 5
	}
    )
