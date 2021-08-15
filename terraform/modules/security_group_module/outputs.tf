# HTTP/HTTPS Security Group ID
output "http_https" {
  value = aws_security_group.http_https.id
}

# Allow all egress Security Group ID
output allow_all_egress {
  value = aws_security_group.allow_all_egress.id
}
