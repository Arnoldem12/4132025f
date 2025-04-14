import boto3
import requests
import pandas as pd
import json
import logging
from botocore.exceptions import ClientError
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PeopleSoftToS3Pipeline:
    def __init__(self, secret_name, region_name, s3_bucket, folder_name):
        """
        Initialize the pipeline with AWS credentials and configuration
        """
        self.secret_name = secret_name
        self.region_name = region_name
        self.s3_bucket = s3_bucket
        self.folder_name = folder_name
        self.session = boto3.session.Session()
        self.secrets_client = self.session.client(
            service_name='secretsmanager',
            region_name=region_name
        )
        self.s3_client = self.session.client('s3')

    def get_secret(self):
        """
        Retrieve credentials from AWS Secrets Manager
        """
        try:
            secret_value = self.secrets_client.get_secret_value(
                SecretId=self.secret_name
            )
            if 'SecretString' in secret_value:
                secret = json.loads(secret_value['SecretString'])
                return secret
        except ClientError as e:
            logger.error(f"Error retrieving secret: {str(e)}")
            raise

    def get_peoplesoft_token(self, base_url, credentials):
        """
        Get authentication token from PeopleSoft
        """
        auth_endpoint = f"{base_url}/auth"
        try:
            response = requests.post(
                auth_endpoint,
                json={
                    "username": credentials["username"],
                    "password": credentials["password"]
                }
            )
            response.raise_for_status()
            return response.json()["token"]
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting PeopleSoft token: {str(e)}")
            raise

    def post_to_peoplesoft(self, base_url, token, endpoint, payload):
        """
        Send POST request to PeopleSoft API
        """
        try:
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
            response = requests.post(
                f"{base_url}/{endpoint}",
                headers=headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error posting to PeopleSoft: {str(e)}")
            raise

    def generate_s3_path(self, timestamp, file_name):
        """
        Generate S3 path with year/month/day folder structure
        """
        year = timestamp.strftime('%Y')
        month = timestamp.strftime('%m')
        day = timestamp.strftime('%d')
        time_suffix = timestamp.strftime('%H%M%S')
        
        return f"{self.folder_name}/year={year}/month={month}/day={day}/{file_name}_{time_suffix}.parquet"

    def save_to_parquet(self, data, s3_path):
        """
        Convert data to Parquet and save to S3
        """
        try:
            # Convert to DataFrame
            df = pd.DataFrame(data)
            
            # Convert to parquet in memory
            parquet_buffer = df.to_parquet()
            
            # Upload to S3
            self.s3_client.put_object(
                Bucket=self.s3_bucket,
                Key=s3_path
            )
            logger.info(f"Successfully saved data to s3://{self.s3_bucket}/{s3_path}")
        except Exception as e:
            logger.error(f"Error saving to parquet: {str(e)}")
            raise

    def run_pipeline(self, base_url, endpoint, payload, file_name):
        """
        Execute the complete pipeline
        """
        try:
            # Get credentials from Secrets Manager
            credentials = self.get_secret()
            
            # Get PeopleSoft token
            token = self.get_peoplesoft_token(base_url, credentials)
            
            # Send POST request to PeopleSoft
            response_data = self.post_to_peoplesoft(base_url, token, endpoint, payload)
            
            # Generate S3 path with hierarchical structure
            current_time = datetime.now()
            s3_path = self.generate_s3_path(current_time, file_name)
            
            # Save response to S3 as parquet
            self.save_to_parquet(response_data, s3_path)
            
            return f"s3://{self.s3_bucket}/{s3_path}"
        except Exception as e:
            logger.error(f"Pipeline failed: {str(e)}")
            raise

def main():
    # Configuration
    SECRET_NAME = "peoplesoft/credentials"
    REGION_NAME = "us-east-1"
    S3_BUCKET = "your-bucket-name"
    BASE_URL = "https://your-peoplesoft-instance.com/api"
    ENDPOINT = "your-endpoint"
    FOLDER_NAME = "peoplesoft_data"  # Root folder name
    FILE_NAME = "data_extract"  # Base file name
    
    # Example payload for the POST request
    PAYLOAD = {
        "query": "your query here",
        "parameters": {
            # Add your parameters here
        }
    }
    
    # Initialize and run pipeline
    pipeline = PeopleSoftToS3Pipeline(SECRET_NAME, REGION_NAME, S3_BUCKET, FOLDER_NAME)
    try:
        output_path = pipeline.run_pipeline(BASE_URL, ENDPOINT, PAYLOAD, FILE_NAME)
        logger.info(f"Pipeline completed successfully. Data saved to {output_path}")
    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()