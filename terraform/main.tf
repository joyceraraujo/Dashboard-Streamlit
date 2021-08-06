# from : https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance

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

    ingress {
  
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  from_port         = 80
  to_port           = 80

  }
    ingress {
  
  protocol          = "tcp"
  ipv6_cidr_blocks = ["::/0"]
  from_port         = 80
  to_port           = 80

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

resource "aws_instance" "ec2-streamlit_tf" {
  ami           =  "ami-0c2b8ca1dad447f8a"//data.aws_ami.ubuntu.id
  instance_type = "t2.micro"
  vpc_security_group_ids = [aws_security_group.streamlit-sg.id]
  user_data = file("init-script.sh")
  tags = {
    Name = "ec2-streamlit_tf"
  }
}


