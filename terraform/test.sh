#!/bin/bash
#A quick post deploy check to ensure the ELB is online, currently returns a 503 as there are no backend services at present

echo "Starting Test"
response=$(curl --write-out '%{http_code}' --silent --output /dev/null `terraform output elb_dns_name | sed -e 's/"//g'` -k)
if [ $response == 503 ]
then
  echo "Passed"
else
  eccho "Failed"
fi
echo "Finished"
