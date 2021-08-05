# from : https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance
data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_security_group" "streamlit-sg" {
  name        = "streamlit-sg"
  description = "Allow streamlit traffic"
  

  ingress {
  
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  from_port         = 8501
  to_port           = 8501

  }
 ingress {
  
  protocol          = "tcp"
  ipv6_cidr_blocks = ["::/0"]
  from_port         = 8501
  to_port           = 8501

  }
 ingress {
  
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  from_port         = 22
  to_port           = 22

  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    //ipv6_cidr_blocks = ["::/0"]
  }


  tags = {
    Name = "streamlit"
  }
}

resource "aws_instance" "ec2-streamlit" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t2.micro"
  vpc_security_group_ids = [aws_security_group.streamlit-sg.id]
  tags = {
    Name = "ec2-streamlit"
  }
}


