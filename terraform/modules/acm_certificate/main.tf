####################
# Self Signed Cert for the ELB
####################
resource "tls_private_key" "example" {
  algorithm = var.key_algorithm
}

resource "tls_self_signed_cert" "example" {
  key_algorithm   = var.key_algorithm
  private_key_pem = tls_private_key.example.private_key_pem

  subject {
    common_name  = var.certificate_common_name
    organization = var.certificate_organisation
  }

  validity_period_hours = 12

  allowed_uses = [
    "key_encipherment",
    "digital_signature",
    "server_auth",
  ]
}

resource "aws_acm_certificate" "cert" {
  private_key      = tls_private_key.example.private_key_pem
  certificate_body = tls_self_signed_cert.example.cert_pem
}
