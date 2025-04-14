import boto3
import pandas as pd
from io import StringIO

# Create session
s3 = boto3.client('s3')
bucket = 'data-pipeline-bucket-xxxx'
source_key = 'input/customer_data.csv'
destination_key = 'output/cleaned_data.csv'

# Load CSV
obj = s3.get_object(Bucket=bucket, Key=source_key)
df = pd.read_csv(obj['Body'])

# Clean data
df.dropna(inplace=True)
df['full_name'] = df['first_name'] + ' ' + df['last_name']

# Write back to S3
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)

s3.put_object(
    Bucket=bucket, 
    Key=destination_key, 
    Body=csv_buffer.getvalue()
)