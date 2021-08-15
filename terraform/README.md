# README.md

This codebase pulls in various modules to build a VPC environment consisting of:
 - A VPC
 - Public & Private Subnets per Availability Zone in the Region
 - NAT & Internet Gateways
 - An ELB
 - A Security Group exposing port 443/80 attached to the ELB
 - A Certificate created in ACM and attached to the ELB

This codebase uses terraform-docs to generate the README.

Requirements: Terraform 1.0.3

Running a Terraform Plan:
```bash
sh run_plan.sh
```

Running a Terraform Apply:
```bash
terraform apply dev.plan
```

### Linting

```bash
tflint --module --var-file=tfvars/dev.tfvars
```

### tfsec
```bash
tfsec .
```

### Terraform validate and check
```bash
terraform validate
```
```bash
terraform fmt --check
```

## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | 3.54.0 |

## Providers

No providers.

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_elb"></a> [elb](#module\_elb) | ./modules/elb_module | n/a |
| <a name="module_elb_certificate"></a> [elb\_certificate](#module\_elb\_certificate) | ./modules/acm_certificate | n/a |
| <a name="module_route53"></a> [route53](#module\_route53) | ./modules/route53 | n/a |
| <a name="module_security_groups"></a> [security\_groups](#module\_security\_groups) | ./modules/security_group_module | n/a |
| <a name="module_vpc"></a> [vpc](#module\_vpc) | ./modules/vpc_module | n/a |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_environment"></a> [environment](#input\_environment) | The name of the environment | `string` | n/a | yes |
| <a name="input_public_route53_domain"></a> [public\_route53\_domain](#input\_public\_route53\_domain) | The Domain to be used for Route53 | `string` | n/a | yes |
| <a name="input_region"></a> [region](#input\_region) | The region to deploy to | `string` | `"eu-west-1"` | no |
| <a name="input_tags"></a> [tags](#input\_tags) | Common tags used throughout the environment | `map` | n/a | yes |
| <a name="input_vpc_cidr"></a> [vpc\_cidr](#input\_vpc\_cidr) | CIDR of the VPC | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_elb_dns_name"></a> [elb\_dns\_name](#output\_elb\_dns\_name) | The DNS Name for the ELB created |
| <a name="output_private_subnet_ids"></a> [private\_subnet\_ids](#output\_private\_subnet\_ids) | List of IDs for the private subnets |
| <a name="output_public_subnet_ids"></a> [public\_subnet\_ids](#output\_public\_subnet\_ids) | List of IDs for the public subnets |
| <a name="output_vpc_id"></a> [vpc\_id](#output\_vpc\_id) | ID of the VPC |
