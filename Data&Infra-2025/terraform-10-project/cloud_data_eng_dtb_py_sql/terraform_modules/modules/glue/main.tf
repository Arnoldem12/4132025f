variable "job_name" {}
variable "s3_bucket_name" {}

resource "aws_glue_job" "this" {
  name     = var.job_name
  role_arn = aws_iam_role.glue_role.arn
  command {
    script_location = "s3://${var.s3_bucket_name}/scripts/etl_script.py"
    name            = "glueetl"
  }
}

resource "aws_iam_role" "glue_role" {
  name = "glue-job-role"

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