#!/bin/bash

terraform validate
terraform fmt --check
tflint --module --var-file=tfvars/dev.tfvars
tfsec
