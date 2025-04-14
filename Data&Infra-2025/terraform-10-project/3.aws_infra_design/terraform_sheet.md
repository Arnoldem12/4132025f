# Terraform AWS Cheatsheet

## 📌 Providers
```hcl
provider "aws" {
  region = "us-east-1"
}
```

## 🌐 VPC
```hcl
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  name = "my-vpc"
  cidr = "10.0.0.0/16"
  azs  = ["us-east-1a", "us-east-1b"]
  public_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
}
```

## 💻 EC2 Instance
```hcl
resource "aws_instance" "example" {
  ami = "ami-123456"
  instance_type = "t2.micro"
  tags = { Name = "MyInstance" }
}
```

## 🛡️ IAM Role
```hcl
resource "aws_iam_role" "lambda_role" {
  name = "lambda_exec"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": { "Service": "lambda.amazonaws.com" },
    "Action": "sts:AssumeRole"
  }]
}
EOF
}
```

## 🗄️ RDS Instance
```hcl
resource "aws_db_instance" "default" {
  allocated_storage = 20
  engine = "mysql"
  instance_class = "db.t3.micro"
  name = "mydb"
  username = "admin"
  password = "MyPassword123"
  skip_final_snapshot = true
}
```

## 📁 Outputs
```hcl
output "bucket_name" {
  value = aws_s3_bucket.my_bucket.id
}
```