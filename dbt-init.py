#!/usr/bin/env python
from argparse import ArgumentParser
import sys
import os
import re
import shutil

import jinja2

# Use the pattern:
# path = dir_path + dir
starter_project_dir_path = os.path.dirname(__file__)
starter_project_dir = "starter-project"
starter_project_path = os.path.join(starter_project_dir_path, starter_project_dir)


class OperationalError(Exception):
    def __init__(self, message):
        self.message = message
        super(OperationalError, self).__init__(message)


def render_template(dir_path, filename, parsed):
    """ Load the starter project and render the project details """
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(dir_path), undefined=jinja2.StrictUndefined
    )

    loaded = environment.get_template(filename)

    rendered = loaded.render(project=parsed)
    return rendered


def write_file(file_path, contents):
    path, file = os.path.split(file_path)
    if not os.path.exists(path):
        os.makedirs(path)
    f = open(file_path, "w")
    f.write(contents)


def parse_args(args):
    parser = ArgumentParser(description="dbt project starter")
    parser.add_argument(
        "--client",
        required=True,
        help="The name of the client you are creating this project for",
    )
    parser.add_argument(
        "--warehouse",
        choices=["postgres", "redshift", "snowflake", "bigquery"],
        help="The warehouse your client is using",
    )
    parser.add_argument(
        "target_dir",
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
    if not os.path.exists(parsed.target_dir):
        raise OperationalError(
            "Target directory {} does not exist!".format(parsed.target_dir)
        )

    # set the path we are targeting
    client_project_dir = "{}-dbt".format(parsed.client.replace("_", "-"))
    client_project_path = os.path.join(parsed.target_dir, client_project_dir)
    os.mkdir(client_project_path)

    # for each file in the starter project, copy a rendered version of the file
    for subdir, dirs, files in os.walk(starter_project_path):
        for file in files:
            rendered_template = render_template(subdir, file, parsed)
            target_dir = subdir.replace(starter_project_path, client_project_path)
            target_filepath = os.path.join(target_dir, file)
            write_file(target_filepath, rendered_template)
    
    print("New dbt project for {} created at {}! 🎉".format(parsed.client, client_project_path))


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parsed = parse_args(args)

    handle(parsed)


if __name__ == "__main__":
    main()
