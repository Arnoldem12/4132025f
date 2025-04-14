# etl data glue from sql to aws

Import boto3
import pandas as pd
import sqlalchemy
import pyodbc
import os
import datetime
import logging
import json
import requests
import time
import re
import numpy as np


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set up AWS credentials and region 
boto3.setup_default_session(
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    region_name=os.environ.get('AWS_REGION')
)
s3 = boto3.client('s3')
glue = boto3.client('glue') 

# Set up SQL Server connection parameters
sql_server = 'arnol_sql_server'  # Replace with your SQL Server endpoint    
sql_database = 'arnoldb'  # Replace with your SQL Server database name
sql_username = os.environ.get('SQL_USERNAME')  # Replace with your SQL Server username  
sql_password = os.environ.get('SQL_PASSWORD')  # Replace with your SQL Server password
sql_driver = '{ODBC Driver 17 for SQL Server}'  # Replace with your SQL Server ODBC driver
sql_port = 1433  # Default SQL Server port  

sql_connection_string = f"mssql+pyodbc://{sql_username}:{sql_password}@{sql_server}:{sql_port}/{sql_database}?driver={sql_driver}"
engine = sqlalchemy.create_engine(sql_connection_string)
conn = engine.connect()

# Set up S3 bucket and Glue job parameters
s3_bucket = 'your-s3-bucket-name'  # Replace with your S3 bucket name
s3_prefix = 'your-s3-prefix/'  # Replace with your S3 prefix (folder path)
glue_job_name = 'your-glue-job-name'  # Replace with your Glue job name
glue_database_name = 'your-glue-database-name'  # Replace with your Glue database name
glue_table_name = 'your-glue-table-name'  # Replace with your Glue table name
glue_output_path = f"s3://{s3_bucket}/{s3_prefix}"  # S3 path for Glue job output   

# Set up SQL query to extract data from SQL Server
sql_query = "SELECT * FROM your_table_name"  # Replace with your SQL query
# sql_query = "SELECT * FROM your_table_name WHERE condition"  # Example with a WHERE clause
