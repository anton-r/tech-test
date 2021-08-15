output "cert_id" {
  description = "The ID of the certificate created"
  value = aws_acm_certificate.cert.id
}
