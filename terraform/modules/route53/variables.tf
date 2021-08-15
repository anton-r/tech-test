# The domain name for the Public Route53 zone
variable public_route53_domain {
  description = "The Domain Name for Route53"
  type = string
}

# The environment name
variable environment {
  description = "The name of the environment"
  type = string
}

# DNS name of the ELB created in the ELB module
variable elb_dns_name {
  description = "ELB DNS Name to be associated with the www record"
  type = string
}

# ELB Zone ID to be passed to the route53 record
variable elb_zone_id {
  description = "ELB Zone ID to be used in the www record"
  type = string
}

# Tags
variable tags {
  description = "Common tags used throughout the environment"
  type = map
}
