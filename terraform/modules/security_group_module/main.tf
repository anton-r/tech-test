####################
# Security Group for inbound HTTP/S
####################
resource "aws_security_group" "http_https" {
  name = "${var.environment}-http-https"
  description = "Security Group to allow access to port 443 and 80 externally"
  vpc_id = var.vpc_id
  tags = merge(tomap({Name = "sg-${var.environment}-http-https"}), var.tags)
  ingress {
    protocol = "TCP"
    from_port = 443
    to_port  = 443
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    protocol = "TCP"
    from_port = 80
    to_port  = 80
    cidr_blocks = ["0.0.0.0/0"]
  }
}

####################
# Security Group to allow all outbound traffic
####################
resource "aws_security_group" "allow_all_egress" {
  name = "${var.environment}-allow-all-egress"
  description = "Security Group allow all egress traffic"
  vpc_id = var.vpc_id
  tags = merge(tomap({Name = "sg-${var.environment}-allow-all-egress"}), var.tags)
  egress {
    protocol = "TCP"
    from_port = 0
    to_port  = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}
