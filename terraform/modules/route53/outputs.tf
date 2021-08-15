# The Route 53 Zone ID
output "aws_route53_public_zone_id" {
  value = aws_route53_zone.public.id
}

