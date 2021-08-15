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
  description = "Common tags used throughout the environment"
  type = map
}

# Subnet IDs
variable subnet_ids {
  description = "The Subnet Ids for the ELB"
  type = list
}

# Security Groups
variable security_group {
  description = "The security Groups to be applied to the ELB"
  type = list
}

# Dynamic Listeners
variable listeners {
  type = list(object({
    lb_protocol        = string
    lb_port            = number
    instance_protocol  = string
    instance_port      = number
    ssl_certificate_id = string
  }))
}

# ELB Name
variable name {
  description = "The Name for the ELB"
  type = string
}

# A description for the ELB
variable description {
  description = "The LoadBalancer Description"
  type = string
}

# The Health Check Target
variable health_check_target {
  description = "The ELB Health Check target"
  type = string
}
