import boto3
import json


def get_values(secret_arn: str):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(
        SecretId=secret_arn
    )
    return json.loads(response['SecretString'])
