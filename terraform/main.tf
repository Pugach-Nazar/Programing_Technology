terraform {
  required_version = ">=0.13.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {
    bucket = "lab6-bucket-terraform"
    key = "terraform.tfstate"
    region = "us-east-1"
    dynamodb_table = "lab6-lock-id-table"
  }
}

# Configure the AWS provider
provider "aws" {
  region     = "us-east-1"
}

resource "aws_security_group" "web_app" {
  name        = "web_app"
  description = "security group"
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

 ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags= {
    Name = "web_app"
  }
}

resource "aws_instance" "webapp_instance" {
  ami           = "ami-0866a3c8686eaeeba"
  instance_type = "t2.micro"
  security_groups= ["web_app"]
  user_data = <<-EOF
  #!/bin/bash
  sudo apt update
  sudo apt install docker.io
  y
  docker run -id qwertyasd0933/pawnshop
  EOF
  tags = {
    Name = "webapp_instance"
  }
}

output "instance_public_ip" {
  value     = aws_instance.webapp_instance.public_ip
  sensitive = true
}
