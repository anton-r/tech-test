#!/bin/bash
# Bootstrap script to install correct versions & Tools for the repository

wget https://releases.hashicorp.com/terraform/1.0.3/terraform_1.0.3_darwin_amd64.zip /tmp/.
unzip /tmp/terraform_1.0.3_darwin_amd64.zip /usr/local/bin/.
go install github.com/aquasecurity/tfsec/cmd/tfsec@latest
curl https://raw.githubusercontent.com/terraform-linters/tflint/master/install_linux.sh | bash
