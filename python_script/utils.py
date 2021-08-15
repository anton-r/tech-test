from pathlib import Path
import boto3
from not_used_operations import not_used_operations
from ignore_words import ignore_words

def create_dir(epoch_time):
    """Create the directory for the data and logs"""
    Path(f"./data/{epoch_time}").mkdir(parents=True,exist_ok=True)

def filter_ops(operations):
    """Filter the operations before we run them"""
    filtered_operations = []
    for operation in operations:
        for ignore in ignore_words:
            if ignore in operation:
                #Should be added to some form of ignore log so we can inspect
                continue
            filtered_operations.append(operation)
    return filtered_operations

def get_command(client, command):
    """Execute an operation against the provided Boto Client"""
    return getattr(client, command)()

def tidy_response(response):
    if 'requestId' in response:
        response.pop('requestId')
    response.pop('ResponseMetadata')
    return response


def get_operations(service, region=None, profile=None):
    """Return a list of function calls that can be made. This is filtered against the not used operations data"""
    info_words = ['Describe', 'Get', 'List']
    client = boto3.Session(region_name=region, profile_name=profile).client(service)
    operations = []
    for operation in sorted(client.meta.service_model.operation_names):
        if not any(operation.startswith(prefix) for prefix in info_words):
            continue
        api_methods = dict((v, k) for k, v in client.meta.method_to_api_mapping.items())
        if operation in api_methods:
            op_to_run = api_methods.get(operation)
        try:
            if op_to_run in not_used_operations[service]:
                continue
        except Exception:
            #If the service doesn't have any blacklisted ops we get a KeyError so Continue
            pass

        operations.append(op_to_run)
    return operations

def get_services():
    """Return a list of all of services available from boto3"""
    return [service for service in sorted(boto3.Session().get_available_services())]

def get_regions():
    """Return a list of all of services available from boto3"""
    return [service for service in sorted(boto3.Session().get_available_regions('ec2'))]
