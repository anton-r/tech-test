####################
# Public Route 53 Zone
####################
resource "aws_route53_zone" "public" {
  name = var.public_route53_domain

  tags = merge(tomap({Name = var.environment}), var.tags)
}

####################
# Route 53 record for the ELB
####################
resource "aws_route53_record" "www" {
  zone_id = aws_route53_zone.public.id
  name    = "elb.${var.public_route53_domain}"
  type    = "CNAME"

  alias {
    name                   = var.elb_dns_name
    zone_id                = var.elb_zone_id
    evaluate_target_health = true
  }
}
