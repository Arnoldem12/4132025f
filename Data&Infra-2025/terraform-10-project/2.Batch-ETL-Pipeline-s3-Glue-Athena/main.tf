provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "raw_bucket" {
  bucket = "batch-etl-raw-bucket-123456"
}

resource "aws_s3_bucket" "clean_bucket" {
  bucket = "batch-etl-clean-bucket-123456"
}

resource "aws_glue_catalog_database" "data_db" {
  name = "batch_etl_db"
}

resource "aws_glue_catalog_table" "raw_table" {
  name          = "raw_sales_data"
  database_name = aws_glue_catalog_database.data_db.name
  table_type    = "EXTERNAL_TABLE"

  storage_descriptor {
    location      = "s3://${aws_s3_bucket.raw_bucket.bucket}/sales/"
    input_format  = "org.apache.hadoop.mapred.TextInputFormat"
    output_format = "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat"

    ser_de_info {
      name                  = "OpenCSVSerde"
      serialization_library = "org.apache.hadoop.hive.serde2.OpenCSVSerde"
    }

    columns {
      name = "order_id"
      type = "string"
    }

    columns {
      name = "amount"
      type = "double"
    }

    columns {
      name = "order_date"
      type = "string"
    }
  }
}

resource "aws_iam_role" "glue_role" {
  name = "glue_batch_etl_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = {
        Service = "glue.amazonaws.com"
      },
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_glue_job" "batch_etl" {
  name     = "batch-etl-job"
  role_arn = aws_iam_role.glue_role.arn

  command {
    name            = "glueetl"
    script_location = "s3://${aws_s3_bucket.raw_bucket.bucket}/scripts/glue_etl_script.py"
    python_version  = "3"
  }

  default_arguments = {
    "--TempDir" = "s3://${aws_s3_bucket.raw_bucket.bucket}/temp/"
    "--job-language" = "python"
  }

  max_retries = 1
  glue_version = "3.0"
  number_of_workers = 2
  worker_type = "Standard"
}