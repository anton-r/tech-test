#!/usr/bin/env python
from argparse import ArgumentParser
from utils import get_services
from utils import get_regions
from run_aws import run_aws
from show_more_info import show_more_info

def main():
    """Parse CLI arguments to filter a run by services or region"""
    parser = ArgumentParser(
        prog='aws_estate_checker',
        description=(
            'List AWS resources on one account across regions and services supplied. '
            'The JSON response is saved to ./data/<timestamp>/<region>.'
        )
    )
    subparsers = parser.add_subparsers(
        description='List of subcommands. Use <subcommand> --help for more parameters',
        dest='command',
        metavar='COMMAND'
    )

    run = subparsers.add_parser('run', description='Run the script against AWS',
        help='Discover your AWS Resources')

    run.add_argument(
        '-s',
        '--service',
        action='append',
        help='A service to run against'
    )

    run.add_argument(
        '-r',
        '--region',
        action='append',
        help='A region to run against'
    )

    show_details = subparsers.add_parser('show_details',
        description='Output each type of resources found for a service',
        help='List all resource types found for a given service')

    show_details.add_argument(
        '-t',
        '--timestamp',
        action='store',
        help='The timestamp of the run you wish to look at'
    )

    show_details.add_argument(
        '-s',
        '--service',
        action='append',
        help='A service to display'
    )

    show_details.add_argument(
        '-r',
        '--region',
        action='append',
        help='The region you would like the information for'
    )

    show_details.add_argument(
        '-j',
        '--json',
        action='store_true',
        help='Print the JSON'
    )

    args = parser.parse_args()

    if args.command == 'run':
        services = args.service or get_services()
        regions = args.region or get_regions()
        run_aws(regions,services)

    if args.command == 'show_details':
        timestamp = args.timestamp
        services = args.service
        regions = args.region
        json = args.json or False
        show_more_info(timestamp, services, regions, json)

if __name__ == '__main__':
    exit(main())
