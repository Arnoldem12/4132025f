import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
job.init(args['JOB_NAME'], args)

# Read from raw S3
raw_df = spark.read.option("header", "true").csv("s3://batch-etl-raw-bucket-123456/sales/")

# Basic transformation
clean_df = raw_df.dropna()

# Write cleaned data to clean bucket
clean_df.write.mode("overwrite").parquet("s3://batch-etl-clean-bucket-123456/sales_cleaned/")

job.commit()