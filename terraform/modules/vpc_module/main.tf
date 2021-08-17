/**
  * # README.md
  *
  * This module creates the following:
  *  - A VPC
  *  - Public & Private Subnets per Availability Zone in the Region
  *  - NAT & Internet Gateways
  *
  * This codebase uses terraform-docs to generate the README.
  *
  * To run terraform-docs:
  * ```bash
  *  terraform-docs markdown . | tee README.md
  * ```
  *
  * Requirements: Terraform 1.0.3
  *
  * This module will need to be pulled in to another terraform configuration to be used.
  * Example
  * ```bash
  * module "vpc" {
  *   source = "./modules/vpc_module"
  *   environment = var.environment
  *   tags = var.tags
  *   vpc_cidr = var.vpc_cidr
  * }
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
# Get the available availability zones
####################
data "aws_availability_zones" "available" {
  state = "available"
}

####################
# VPC
####################
resource "aws_vpc" "vpc" {
  cidr_block = var.vpc_cidr
  enable_dns_hostnames = true

  tags = merge(tomap({Name = var.environment}), var.tags)
}

####################
# Internet Gateway & Nat gateways with Elastic IP per AZ
####################
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.vpc.id

  tags = merge(tomap({Name = var.environment}), var.tags)
}

resource aws_eip nat {
  count = length(data.aws_availability_zones.available.names)
  vpc      = true
}

resource aws_nat_gateway nat {
  count = length(data.aws_availability_zones.available.names)
  allocation_id = element(aws_eip.nat.*.id, count.index)
  subnet_id = element(aws_subnet.public_subnet.*.id, count.index)

  tags = merge(tomap({Name = format("%v-nat-%v", var.environment, data.aws_availability_zones.available.names[count.index])}), var.tags)

  depends_on = [aws_eip.nat, aws_internet_gateway.igw, aws_subnet.public_subnet]
}

####################
# Public Subnets Per AZ
####################

resource "aws_subnet" "public_subnet" {
  count = length(data.aws_availability_zones.available.names)
  vpc_id = aws_vpc.vpc.id
  cidr_block = cidrsubnet(var.vpc_cidr, 8, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = true

  tags = merge(tomap({Name =  format("public-%v-%v", var.environment, data.aws_availability_zones.available.names[count.index])}), var.tags)
}

####################
# Private Subnets Per AZ
####################

resource "aws_subnet" "private_subnet" {
  count = length(data.aws_availability_zones.available.names)
  vpc_id = aws_vpc.vpc.id
  cidr_block = cidrsubnet(var.vpc_cidr, 8, count.index + length(data.aws_availability_zones.available.names))
  availability_zone = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = false

  tags = merge(tomap({Name = format("private-%v-%v", var.environment, data.aws_availability_zones.available.names[count.index])}), var.tags)
}

####################
# Public Route Tables Per AZ
####################

resource "aws_route_table" "route" {
  vpc_id = aws_vpc.vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = merge(tomap({Name = format("public-route-table-%v", var.environment)}), var.tags)
}

resource "aws_route_table_association" "route" {
  count = length(data.aws_availability_zones.available.names)
  subnet_id = element(aws_subnet.public_subnet.*.id, count.index)
  route_table_id = aws_route_table.route.id
}

####################
# Private Route Tables
####################

resource "aws_route_table" "private_route" {
  count = length(data.aws_availability_zones.available.names)
  vpc_id = aws_vpc.vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    nat_gateway_id = element(aws_nat_gateway.nat.*.id, count.index)
  }

  tags = merge(tomap({Name = format("private-rt-%v-%v", var.environment, data.aws_availability_zones.available.names[count.index])}), var.tags)
}

resource "aws_route_table_association" "private_route" {
  count = length(data.aws_availability_zones.available.names)
  subnet_id = element(aws_subnet.private_subnet.*.id, count.index)
  route_table_id = element(aws_route_table.private_route.*.id, count.index)
}
