import boto3
import csv
import os

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"] # S3 bucket name
        key = record["s3"]["object"]["key"]
        response = s3.get_object(Bucket=bucket, Key=key)
        lines = response["Body"].read().decode("utf-8").splitlines()
        reader = csv.DictReader(lines)
        for row in reader:
            table.put_item(Item=row)
    return {"statusCode": 200, "body": "Success"}