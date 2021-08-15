#!/usr/bin/env python
import json
import time
from pathlib import Path
from datetime import datetime
import boto3
from ignore_words import ignore_words
from utils import create_dir, get_command, get_operations, tidy_response

def run_aws(regions, services):
    """Takes the list of Services & Regions, Gets the operations and executes them against AWS"""
    print(f'Starting run for: {services} in {regions}')
    epoch_time = int(time.time())
    create_dir(epoch_time)

    ops_log = open(f"./data/{epoch_time}/operations.log", "a")
    error_log = open(f"./data/{epoch_time}/error.log", "a")

    service_dict = {}

    for region in regions:
        service_list = []
        for service in services:
            for operation in get_operations(service, region):

                ops_client = boto3.Session(region_name=region, profile_name=None).client(service)

                try:
                    #See if the operation contains any of the words we want to ignore
                    for ignore in ignore_words:
                        if ignore in operation:
                            #Should be added to some form of ignore log so we can inspect
                            continue

                    #Get the response and remove some of the elements we don't want
                    response = tidy_response(get_command(ops_client, operation))

                    #Some responses come back with just an Empty Array, Ignore for now
                    values_view = response.values()
                    value_iterator = iter(values_view)
                    first_value = next(value_iterator)
                    if first_value in ([], {}):
                        continue
                    #This catches requests that come back with a single element and a count of 0
                    if len(response) == 1 and first_value == 0:
                        continue

                    if region not in service_dict:
                        service_dict[region] = {}
                    if service not in service_list:
                        service_list.append(service)

                    ops_log.write(f"{region} {service} {operation}" + "\n")
                    Path(f"./data/{epoch_time}/{region}").mkdir(parents=True,exist_ok=True)
                    service_data = open(f"./data/{epoch_time}/{region}/{service}-{operation}.json", "w")
                    try:
                        service_data.write(json.dumps(response, indent=2, sort_keys=True, default=datetime.isoformat))
                        service_data.close()
                    except Exception as error:
                        error_log.write(f'ERROR: {service} {operation} {region}- {error}')

                except Exception as error:
                    # Could write this somewhere that's not the error log to enable retry
                    error_log.write(f'ERROR: {service} {operation} {region}- {error}')

            try:
                service_dict[region]["services"] = service_list
            except Exception:
                if region not in service_dict:
                    service_dict[region] = {}

    for region in service_dict:
        print(f'Services in use for Region: {region}')
        for service in service_dict[region]["services"]:
            print(f'{service}')
    print(f'Run Complete, Detailed information is available in JSON at ./data/{epoch_time} and in separate regional folders.')
    ops_log.close()
    error_log.close()
