#!/bin/bash
# Run a plan against the dev environment
terraform workspace select dev
terraform plan --var-file=./tfvars/dev.tfvars -out dev.plan
