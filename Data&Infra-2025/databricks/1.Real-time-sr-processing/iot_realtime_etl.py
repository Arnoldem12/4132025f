# Databricks notebook source
from pyspark.sql.functions import col, to_date, avg
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType

# Step 1: Define schema for incoming JSON data
schema = StructType([
    StructField("device_id", StringType(), True),
    StructField("temperature", DoubleType(), True),
    StructField("humidity", DoubleType(), True),
    StructField("timestamp", TimestampType(), True)
])

# Step 2: Read streaming data using Auto Loader
raw_df = (
    spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "json")
    .schema(schema)
    .load("s3://your-iot-sensor-data-bucket/input/")
)

# Step 3: Clean and transform
clean_df = (
    raw_df
    .na.drop()
    .withColumn("date", to_date(col("timestamp")))
)

# Step 4: Aggregate by day and device
daily_metrics = (
    clean_df
    .groupBy("device_id", "date")
    .agg(
        avg("temperature").alias("avg_temp"),
        avg("humidity").alias("avg_humidity")
    )
)

# Step 5: Write to gold Delta table (batch sink)
query = (
    daily_metrics.writeStream
    .format("delta")
    .outputMode("complete")
    .option("checkpointLocation", "s3://your-iot-sensor-data-bucket/checkpoints/")
    .start("s3://your-iot-sensor-data-bucket/gold/")
)