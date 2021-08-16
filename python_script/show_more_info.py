import os

def show_more_info(timestamp, services, regions, json):
    """Show a list of operations that found resources for a given service,
       in a given region, for a given run"""

    for region in regions:
        print(f'Checking for region {region}')
        directory = f'./data/{timestamp}/{region}'
        check_dir_exists = os.path.isdir(directory)
        if check_dir_exists:
            for filename in os.listdir(directory):
                if any(service in filename for service in services):
                    file_split = filename.split(".")
                    print(f'Data found for {file_split[0]}')

        # Add JSON flag to output JSON if wanted.
        # Need to handle operations.log or timestamp not found

