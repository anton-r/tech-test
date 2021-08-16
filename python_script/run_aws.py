#!/usr/bin/env python
import json
import time
from pathlib import Path
from datetime import datetime
import os
import boto3
from ignore_words import ignore_words
from utils import create_dir, get_command, get_operations, tidy_response
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing.pool import ThreadPool
import multiprocessing
from random import shuffle
from functools import partial
import logging

epoch_time = int(time.time())

def run_aws(regions, services):
    """Takes the list of Services & Regions, Gets the operations and
        executes them against AWS, outputs results and saves to JSON files"""
    print(f'Starting run for: {services} in {regions}')
    global epoch_time
    create_dir(epoch_time)
#     logging.basicConfig(filename = f'./data/{epoch_time}/error.log',level = logging.ERROR)

    ops_to_run = []
    for region in regions:
        Path(f"./data/{epoch_time}/{region}").mkdir(parents=True,exist_ok=True)
        for service in services:
            operations = get_operations(service, region)

            for operation in operations:
                operation_log = open(f'./data/{epoch_time}/operations.json', "a")
                operation_log.write(f'{service} {region} {operation}' + "\n")
                ops_to_run.append([service, region, operation, epoch_time])

            operation_log.close()

    shuffle(ops_to_run)
    print(f'Number of Operations to run: {len(ops_to_run)}\n')

    p = ThreadPool(32)

    #Mullti-thread the requests
    for result in p.imap_unordered(partial(to_run), ops_to_run):
        if result == None:
            continue

        result_region= result["region"]
        result_service = result["service"]
        result_operation = result["operation"]
        result_response = result["response"]

        with open(f"./data/{epoch_time}/{result_region}/{result_service}-{result_operation}.json", "w") as file:
            json.dump(result_response, file, indent=2, sort_keys=True, default=datetime.isoformat)

    for region in regions:
        service_list = []
        result_path = f'./data/{epoch_time}/{region}'
        check_dir_exists = os.path.isdir(result_path)
        if(check_dir_exists):
            for filename in os.listdir(result_path):

                service_name = filename.split('-')[0]

                if service_name not in service_list:
                    service_list.append(service_name)

            print(f'Services in use for Region: {region}')
            for service_to_print in service_list:
                print (f'{service_to_print}')
            print(f'\n')
        else:
            print(f'The results could not be found at ./data/{epoch_time}')

    print(f'Run Complete, Detailed information is available in JSON at ./data/{epoch_time} and in separate regional folders.')


def to_run(op_to_run):
    """Receives operations to run against AWS"""
    service, region, operation, epoch_time = op_to_run

    ops_client = boto3.Session(region_name=region, profile_name=None).client(service)

    try:
        #Get the response and remove some of the elements we don't want
        response = tidy_response(get_command(ops_client, operation))

        #Some responses come back with just an Empty Array, Ignore for now
        values_view = response.values()
        value_iterator = iter(values_view)
        first_value = next(value_iterator)
        if first_value in ([], {}):
            print(f'{operaation} - {response} first_value')
            return
        #This catches requests that come back with a single element that says we have 0 resources
        if len(response) == 1 and first_value == 0:
            print(f'{operaation} - {response} length 1')
            return

        response_dict = {}
        response_dict["service"] = service
        response_dict["operation"] = operation
        response_dict["region"] = region
        response_dict["response"] = response
        return response_dict
    except Exception as error:
    # Could write this somewhere that's not the error log to enable retry
        return

