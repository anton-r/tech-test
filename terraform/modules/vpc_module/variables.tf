# Environment
variable environment {
  description = "The name of the environment"
  type = string
}

# Tags
variable tags {
  description = "Common tags used throughout the environment"
  type = map
}

# Public route53 domain name
variable vpc_cidr {
  description = "CIDR of the VPC"
  type = string
}
