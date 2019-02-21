#!/usr/bin/env python
from argparse import ArgumentParser
import sys
import os
import re
import shutil

import jinja2

dir_path = os.path.dirname(__file__)
starter_project_path = os.path.join(dir_path, "starter-project")


class OperationalError(Exception):
    def __init__(self, message):
        self.message = message
        super(OperationalError, self).__init__(message)


def render_template(dir_path, filename, parsed):
    """ Load a spec. There may be templated password variables, which we render using Jinja. """
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(dir_path),
                                     undefined=jinja2.StrictUndefined)

    loaded = environment.get_template(filename)
    
    rendered = loaded.render(project=parsed)
    return rendered


def parse_args(args):
    parser = ArgumentParser(description="dbt project starter")
    parser.add_argument(
        "--client",
        required=True,
        help="The name of the client you are creating this project for",
    )
    parser.add_argument(
        "--warehouse",
        choices=['postgres','redshift','snowflake', 'bigquery'],
        help="The warehouse your client is using",
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
    os.mkdir(project_path)

    # for each file in the starter project, copy a rendered version of the file
    # will this walk recursively?
    for subdir, dirs, files in os.walk(starter_project_path):
        for file in files:
            rendered_template = render_template(subdir, file, parsed)
            f = open(os.path.join(project_path, file), "w")
            # TODO: replicate nested structure (currently putting everything in one directory)
            f.write(rendered_template)

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parsed = parse_args(args)

    handle(parsed)


if __name__ == "__main__":
    main()
