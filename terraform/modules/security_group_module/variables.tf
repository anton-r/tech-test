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

# VPC CIDR
variable vpc_id {
  description = "The VPC ID"
  type = string
}
