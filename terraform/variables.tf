# The AWS Region
variable region {
  type = string
  description = "The region to deploy to"
  default = "eu-west-1"
}

# Environment
variable environment {
  type = string
  description = "The name of the environment"
}

# Tags
variable tags {
  type = map
  description = "Common tags used throughout the environment"
}

# VPC CIDR
variable vpc_cidr {
  type = string
  description = "CIDR of the VPC"
}

# Route53 Public Domain
variable public_route53_domain {
  type = string
  description = "The Domain to be used for Route53"
}
