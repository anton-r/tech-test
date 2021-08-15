output "vpc_id" {
  description = "ID of the VPC"
  value = module.vpc.vpc_id
}

output "public_subnet_ids" {
  description = "List of IDs for the public subnets"
  value = module.vpc.public_subnet_ids
}

output "private_subnet_ids" {
  description = "List of IDs for the private subnets"
  value = module.vpc.private_subnet_ids
}

output "elb_dns_name" {
  description = "The DNS Name for the ELB created"
  value = module.elb.elb_dns_name
}
