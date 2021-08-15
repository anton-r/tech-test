# Tech Test

## Contents

### Terraform

This repository will deploy the following: 
1. AWS VPC
2. Internet & Nat Gateways
3. 3 Public & Private Subnets (1 per availability zone for resilience & scalability)
4. Routing between the subnets & gateways
5. ELB & Security group for port 443/80
6. Public Route53 Zone and CNAME

The code itself doesn't currently use remote state as this would require some setup as per the remote_state_setup folder.
A S3 Bucket and DynamoDB table are required. To do this you would have to deploy the remote_state_setup code with a local state. Then you can add the following:

```bash
terraform {
   backend "s3" {
     bucket = "<<bucket_name>>"
     key = "terraform.tfstate"
     region = "eu-west-1"
     dynamodb_table = "<<dynamodb_lock_table>>"
   }
}


```
You can add this to the remote_state_setup folder and run terraform init to migrate the remote states state to s3.
For setting this up in production across multiple accounts see here: https://www.terraform.io/docs/language/settings/backends/s3.html

Important Note, A remote state is a must for running from a CI server or multiple people working in an environment.

The modules are not currently in separate repositories here. However in a production environment these folders should be created as standalone repositories and versioned. The module source would then need to look like this:
```bash
module "elb" {
  source = "git@github.com/repository"
  version = 0.1.0
```

TFSec

tfsec is used to scan the code for security issues. In the current state this will fail because the ELB allows unrestricted access in (http/s) and out (0.0.0.0/0 on all ports) of the ELB. To ignore rules for particular resources you can do the below
```bash
####################
# ELB
####################
#tfsec:ignore:AWS005:exp:2022-01-01
```

### Python Script

Interesting task as I hadn't done much scripting in a while. 

Few approaches I looked at first: 
 - Export from Console and evaluate (not scripty)
 - Use Cost Explorer API (Costs)
 - Resource Tagging API (This set me of on a good path but doesn't include all services) 

After getting the services, regions and operations I started to hit errors due to a number of reasons.
I decided to catch these errors and log them. I decided to log the operations along with the output for a while.
This meant I could discover services that either need extra information, or come back with data even with no resources.
I used this to look for common patterns and use this to filter out which commands to run.

Any feedback would be appreciated!
Thanks! 


