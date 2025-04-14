# Databricks notebook source
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.clustering import KMeans
import mlflow
import mlflow.spark

# Step 1: Load customer data from Delta/S3
df = spark.read.format("delta").load("s3://your-customer-data-bucket/input/")

# Optional: drop nulls and cast columns if needed
df_clean = df.dropna()

# Step 2: Feature engineering
feature_cols = ["total_purchases", "average_basket_size", "visit_frequency"]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
assembled_df = assembler.transform(df_clean)

scaler = StandardScaler(inputCol="features", outputCol="scaled_features")
scaler_model = scaler.fit(assembled_df)
scaled_df = scaler_model.transform(assembled_df)

# Step 3: KMeans clustering
with mlflow.start_run():
    kmeans = KMeans(featuresCol="scaled_features", k=4, seed=1)
    model = kmeans.fit(scaled_df)
    clustered = model.transform(scaled_df)

    # Log the model
    mlflow.spark.log_model(model, "kmeans_model")
    mlflow.log_param("k", 4)
    mlflow.log_metric("wssse", model.summary.trainingCost)

    # Step 4: Write clustered results to Delta
    clustered.write.format("delta").mode("overwrite").save("s3://your-customer-data-bucket/output/clusters/")