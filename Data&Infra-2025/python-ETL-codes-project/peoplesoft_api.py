#getting api data from peoplesoft
import requests
import json
import boto3 
import pandas as pd
import os
import logging
from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth
import ssl
import urllib3
import certifi
import pyarrow
import pyarrow.parquet as pq
from botocore.exceptions import ClientError
   

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#initialize aws clients
region_name = os.environ.get('AWS_REGION', 'us-east-1')
session = boto3.Session()
s3_client = boto3.client('s3', region_name=region_name)
secrets_client = boto3.client('secretsmanager', region_name=region_name)
s3_resource = boto3.resource('s3', region_name=region_name) 

def get_secret(secret_name, retries=3, delay=5):
    """
    Retrieve a secret from AWS Secrets Manager.
    """
    for attempt in range(retries):
        try:
            response = secrets_client.get_secret_value(SecretId=secret_name)
            if 'SecretString' in response:
                return json.loads(response['SecretString'])
            else:
                return None
        except ClientError as e:
            if e.response['Error']['Code'] == 'ThrottlingException':
                logger.warning(f"Throttling exception: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                logger.error(f"Error retrieving secret: {e}")
                raise e
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise e
        break   

    # Get s3 bucket and key from environment variables
    bucket_name = os.environ.get('BUCKET_NAME')
    key = os.environ.get('KEY')
    if not bucket_name or not key:
        logger.error("BUCKET_NAME or KEY environment variable not set.")
        raise ValueError("BUCKET_NAME or KEY environment variable not set.")
    # Get the secret value
    secret = get_secret(secret_name)
    if not secret:
        logger.error(f"Secret {secret_name} not found.")
        raise ValueError(f"Secret {secret_name} not found.")
    # Get the username and password from the secret
    # username = secret.get('username')
    # password = secret.get('password')
    # if not username or not password:
    #     logger.error("Username or password not found in secret.")
    #     raise ValueError("Username or password not found in secret.")
    def lambda_handler (event, context):
        """
        AWS Lambda function handler.
        """
        # Get the secret name from the event
        secret_name = event.get('secret_name')
        if not secret_name:
            logger.error("Secret name not provided in event.")
            raise ValueError("Secret name not provided in event.")
        
        # Get the secret value
        secret = get_secret(secret_name)
        if not secret:
            logger.error(f"Secret {secret_name} not found.")
            raise ValueError(f"Secret {secret_name} not found.")
        
        # Get the username and password from the secret
        username = secret.get('username')
        password = secret.get('password')
        if not username or not password:
            logger.error("Username or password not found in secret.")
            raise ValueError("Username or password not found in secret.")
        
        # Set up SSL context to use the system's CA certificates
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        
        # Disable SSL verification for requests (not recommended for production)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        # Make a request to the API using basic authentication
        url = "https://api.example.com/data"
        headers = {"Content-Type": "application/json"}

        response = requests.get(url, auth=HTTPBasicAuth(username, password), headers=headers, verify=False, timeout=10)
        if response.status_code == 200:
            logger.info("API request successful.")
            data = response.json()
            # Convert the data to a DataFrame       
            df = pd.DataFrame(data)
            # Convert the DataFrame to Parquet format   
            table = pyarrow.Table.from_pandas(df)
            pq.write_table(table, '/tmp/data.parquet')
            # Upload the Parquet file to S3
            s3_client.upload_file('/tmp/data.parquet', bucket_name, key)
            logger.info(f"File uploaded to s3://{bucket_name}/{key}")
        else:
            logger.error(f"API request failed with status code {response.status_code}.")
            raise Exception(f"API request failed with status code {response.status_code}.")
        return {
            'statusCode': 200,
            'body': json.dumps('Data processed successfully!')
        }
    # Test the function locally if run as a script
    if __name__ == "__main__":
        event = {
            'secret_name': 'your_secret_name'
        }
        context = {}
        lambda_handler(event, context)
        # Clean up temporary files                                              
        if os.path.exists('/tmp/data.parquet'):
            os.remove('/tmp/data.parquet')
        logger.info("Temporary file cleaned up.")
        # Clean up S3 bucket and key if needed
        # s3_client.delete_object(Bucket=bucket_name, Key=key)  
        # logger.info(f"Deleted s3://{bucket_name}/{key}")
        # Clean up AWS resources if needed
        # s3_resource.Bucket(bucket_name).objects.all().delete()
        # logger.info(f"Deleted all objects in bucket {bucket_name}.")
        # Clean up AWS resources if needed
        # s3_client.delete_bucket(Bucket=bucket_name)   
        # logger.info(f"Deleted bucket {bucket_name}.")
        # Clean up AWS resources if needed
        # s3_client.delete_object(Bucket=bucket_name, Key=key)
        # logger.info(f"Deleted s3://{bucket_name}/{key}")