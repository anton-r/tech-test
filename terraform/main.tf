/**
  * # README.md
  *
  * This codebase pulls in various modules to build a VPC environment consisting of:
  *  - A VPC
  *  - Public & Private Subnets per Availability Zone in the Region
  *  - NAT & Internet Gateways
  *  - An ELB
  *  - A Security Group exposing port 443/80 attached to the ELB
  *  - A Certificate created in ACM and attached to the ELB
  *
  * This codebase uses terraform-docs to generate the README.
  *
  *
  * Requirements: Terraform 1.0.3
  *
  * Running a Terraform Plan:
  * ```bash
  * sh run_plan.sh
  * ```
  *
  * Running a Terraform Apply:
  * ```bash
  * terraform apply dev.plan
  * ```
  *
  * ### Linting
  *
  * ```bash
  * tflint --module --var-file=tfvars/dev.tfvars
  * ```
  *
  * ### tfsec
  * ```bash
  * tfsec .
  * ```
  *
  * ### Terraform validate and check
  * ```bash
  * terraform validate
  * ```
  * ```bash
  * terraform fmt --check
  * ```
  */

####################
# Required Providers
####################
terraform {
  required_providers {
    aws = {
      version = "3.54.0"
    }
  }
}

####################
# AWS Provider
####################
provider "aws" {
  region = var.region
}

####################
# VPC Module
####################
module "vpc" {
  source = "./modules/vpc_module"
  environment = var.environment
  tags = var.tags
  vpc_cidr = var.vpc_cidr

}

####################
# ACM Cert for ELB
####################
module "elb_certificate" {
  source = "./modules/acm_certificate"
  key_algorithm = "RSA"
  certificate_common_name = var.public_route53_domain
  certificate_organisation = "Example"
}

####################
# ELB
####################
# Example of how to skip security warning from tfsec if we need to.
#tfsec:ignore:AWS005:exp:2022-01-01
module "elb" {
  source = "./modules/elb_module"
  environment = var.environment
  tags = var.tags
  subnet_ids = module.vpc.public_subnet_ids
  listeners = [
    {
      lb_protocol        = "HTTP"
      lb_port            = 80
      instance_protocol  = "HTTP"
      instance_port      = 80
      ssl_certificate_id = null
    },
    {
      lb_protocol        = "HTTPS"
      lb_port            = 443
      instance_protocol  = "HTTP"
      instance_port      = 80
      ssl_certificate_id = module.elb_certificate.cert_id
    },
  ]
  health_check_target = "TCP:80"
  security_group = [module.security_groups.http_https,module.security_groups.allow_all_egress]
  description = "A General ELB"
  name = "general"
}

####################
# Security Group
####################
module "security_groups" {
  source = "./modules/security_group_module"
  environment = var.environment
  tags = var.tags
  vpc_id = module.vpc.vpc_id
}

####################
# Route53
####################
module "route53" {
  source = "./modules/route53"
  environment = var.environment
  elb_zone_id = module.elb.elb_zone_id
  elb_dns_name = module.elb.elb_dns_name
  tags = var.tags
  public_route53_domain = var.public_route53_domain
}
