provider "aws" {
  region = "us-east-1"
}

module "s3_bucket" {
  source  = "./modules/s3"
  bucket_name = "data-pipeline-bucket-${random_id.bucket_id.hex}"
}

resource "random_id" "bucket_id" {
  byte_length = 4
}

module "glue_job" {
  source         = "./modules/glue"
  job_name       = "etl-job"
  s3_bucket_name = module.s3_bucket.bucket_name
}