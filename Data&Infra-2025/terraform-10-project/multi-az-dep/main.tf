#Define a VPC that spans multiple AZs
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public" {
  count             = length(var.availability_zones)
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(aws_vpc.main.cidr_block, 8, count.index)
  availability_zone = var.availability_zones[count.index]
  
  tags = {
    Name = "Public-${var.availability_zones[count.index]}"
  }
}

resource "aws_subnet" "private" {
  count             = length(var.availability_zones)
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(aws_vpc.main.cidr_block, 8, count.index + length(var.availability_zones))
  availability_zone = var.availability_zones[count.index]
  
  tags = {
    Name = "Private-${var.availability_zones[count.index]}"
  }
}

#Create multi-AZ resources where appropriate
resource "aws_db_instance" "database" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t3.micro"
  multi_az             = true
  db_subnet_group_name = aws_db_subnet_group.default.name
}

resource "aws_db_subnet_group" "default" {
  name       = "main"
  subnet_ids = aws_subnet.private[*].id
}

resource "aws_lb" "application" {
  name               = "app-lb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.lb.id]
  subnets            = aws_subnet.public[*].id
  
  enable_deletion_protection = true
}

#Implement Auto Scaling Groups that span multiple AZs
resource "aws_launch_configuration" "app" {
  name_prefix     = "app-"
  image_id        = var.ami_id
  instance_type   = "t3.micro"
  security_groups = [aws_security_group.app.id]
  
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "app" {
  name                 = "app-asg"
  launch_configuration = aws_launch_configuration.app.name
  min_size             = 2
  max_size             = 10
  desired_capacity     = 2
  vpc_zone_identifier  = aws_subnet.private[*].id
  
  target_group_arns    = [aws_lb_target_group.app.arn]
  health_check_type    = "ELB"
  
  lifecycle {
    create_before_destroy = true
  }
}