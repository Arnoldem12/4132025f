from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper

spark = SparkSession.builder.appName("ETL").getOrCreate()

df = spark.read.option("header", True).csv("s3a://your-bucket/input.csv")
df_clean = df.dropna().withColumn("UPPER_NAME", upper(col("customer_name")))
df_clean.write.format("delta").save("s3a://your-bucket/output/")