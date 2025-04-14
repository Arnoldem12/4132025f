output "raw_bucket_name" {
  value = aws_s3_bucket.raw_bucket.id
}

output "clean_bucket_name" {
  value = aws_s3_bucket.clean_bucket.id
}

output "glue_job_name" {
  value = aws_glue_job.batch_etl.name
}