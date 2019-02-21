#!/usr/bin/env python
from argparse import ArgumentParser
import sys
import os
import re
import shutil

dir_path = os.path.dirname(__file__)
starter_project_path = os.path.join(dir_path, "starter-project")


class OperationalError(Exception):
    def __init__(self, message):
        self.message = message
        super(OperationalError, self).__init__(message)


def parse_args(args):
    parser = ArgumentParser(description="dbt project starter")
    parser.add_argument(
        "--client",
        required=True,
        help="The name of the client you are creating this project for",
    )
    parser.add_argument(
        "target_directory",
        help="The target directory name. Note that the project will be created as a subdirectory within the target directory",
    )

    parsed = parser.parse_args(args)
    return parsed


def handle(parsed):
    """Something something
    """
    # check that the client name only contains letters and underscores
    if not re.match("^[a-z0-9_]*$", parsed.client):
        raise OperationalError(
            'Client "{}" should only contain lower case letters, numbers, and underscores.'.format(
                parsed.client
            )
        )

    # check that the target directory is valid
    if not os.path.exists(parsed.target_directory):
        raise OperationalError(
            "Target directory {} does not exist!".format(parsed.target_directory)
        )

    # create a directory named target_directory/<client>-dbt
    project_directory = "{}-dbt".format(parsed.client.replace("_", "-"))
    project_path = os.path.join(parsed.target_directory, project_directory)

    # Copy the contents of the `starter-project` directory into the target directory
    shutil.copytree(starter_project_path, project_path)

    print(
        "Starter project for {} succesfully created at {}".format(
            parsed.client, project_path
        )
    )


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parsed = parse_args(args)

    handle(parsed)


if __name__ == "__main__":
    main()
