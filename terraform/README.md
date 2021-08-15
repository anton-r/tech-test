# README.md

This codebase pulls in various modules to build a VPC environment consisting of:
 - A VPC
 - Public & Private Subnets
 - NAT & Internet Gateways
 - An ELB
 - A Security Group exposing port 443/80 attached to the ELB
 - A Certificate created in ACM and attached to the ELB

## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | 1.0.3 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | 3.54.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="requirement_tls"></a> [tls](#requirement\_tls) | 3.1.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | 3.54.0 |


## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_elb"></a> [elb](#module\_elb) | ./modules/elb_module | n/a |
| <a name="module_elb_certificate"></a> [elb\_certificate](#module\_elb\_certificate) | ./modules/acm_certificate | n/a |
| <a name="module_security_group_elb"></a> [security\_group\_elb](#module\_security\_group\_elb) | ./modules/security_group_module | n/a |
| <a name="module_vpc"></a> [vpc](#module\_vpc) | ./modules/vpc_module | n/a |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_environment"></a> [environment](#input\_environment) | The name of the environment | `string` | n/a | yes |
| <a name="input_region"></a> [region](#input\_region) | The region to deploy to | `string` | `"eu-west-1"` | no |
| <a name="input_tags"></a> [tags](#input\_tags) | Common tags used throughout the environment | `map` | n/a | yes |
| <a name="input_vpc_cidr"></a> [vpc\_cidr](#input\_vpc\_cidr) | CIDR of the VPC | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_private_subnet_ids"></a> [private\_subnet\_ids](#output\_private\_subnet\_ids) | List of IDs for the private subnets |
| <a name="output_public_subnet_ids"></a> [public\_subnet\_ids](#output\_public\_subnet\_ids) | List of IDs for the public subnets |
| <a name="output_vpc_id"></a> [vpc\_id](#output\_vpc\_id) | ID of the VPC |
