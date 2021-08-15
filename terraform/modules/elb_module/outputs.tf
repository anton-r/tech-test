output elb_id {
  description = "ID of the LoadBalancer created"
  value = aws_elb.elb.id
}

output elb_dns_name {
  description = "The name of the ELB"
  value = aws_elb.elb.dns_name
}

output elb_zone_id {
  description = "The ELB Zone ID"
  value = aws_elb.elb.zone_id
}
