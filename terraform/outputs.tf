output "domain-name" {
  value = aws_instance.ec2-streamlit_tf.public_dns
}

output "application-url" {
   value = "http://${aws_instance.ec2-streamlit_tf.public_dns}:8501"
}