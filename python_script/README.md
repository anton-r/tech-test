# AWS Estate Checker

This script gets all AWS services running region wise and displays them. It is a WIP and needs to be optimized for running against all of the services for all regions in AWS.

The script currently:
1. Gets the list of services / parses the provided services
2. Gets the list of regions / parses the provided regions
3. Gets the operations for those services
4. Runs the operation
5. Catches any errors and sends to the error log
6. Logs the operations being ran - This could be compared to see if new services/operations are appearing. Or also be used to build in a re-run feature
7. Writes json files of the response for downstream consumption (This could be loaded into redshift using s3 and json path files) or transformed to be displayed.

### To-Dos
 - Optimization/Multithreading - A feature that would need adding before running against entire aws estate in one run at the moment
 - Filter out default resources created by AWS
 - Better output, do something with the JSON files to show detailed information in a prettier way.  
 - Don't run the ops for every service in every region to reduce requests   
 - Re-run using the Ops log
 - Diff from previous run to provide some more useful output
 - Auto versioning / Changelog
 - Handle operations that require extra parameters
 - Better exception catching/handling

### Requirements
 - Python 3.8.11

### Running the script
```bash
 python __main__.py run --service ec2 --service s3 --service securityhub --region eu-west-1 --region us-east-1
```

If you do run without filters for now, it will take a while to run! 

### Example Script Output
```bash
Starting run for: ['ec2', 's3', 'securityhub'] in ['eu-west-1', 'eu-west-2']
Services in use for Region: eu-west-1
ec2
s3
Services in use for Region: eu-west-2
ec2
s3
Run Complete, Detailed information is available in JSON at ./data/1629054923 and in separate regional folders.
```

### Example JSON file
```bash
▶ cat ./data/1629054923/eu-west-1/s3-list_buckets.json 
{
  "Buckets": [
    {
      "CreationDate": "2021-08-15T17:06:20+00:00",
      "Name": "test-bucket-anton-reid"
    }
  ],
  "Owner": {
    "DisplayName": "antreid91",
    "ID": "29efdaff451fc6d44637f07062a4ae0c6576e73db3294c205bbbdc4365f384cf"
  }
}
```
