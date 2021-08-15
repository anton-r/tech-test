#!/usr/bin/env python
from argparse import ArgumentParser
from utils import get_services
from utils import get_regions
from run_aws import run_aws

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

    args = parser.parse_args()

    if args.command == 'run':
        services = args.service or get_services()
        regions = args.region or get_regions()
        run_aws(regions,services)

if __name__ == '__main__':
    exit(main())
