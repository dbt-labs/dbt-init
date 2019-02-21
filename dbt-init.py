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


def render_template(dir_path, filename, project):
    """ Load the starter project and render the project details """
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(dir_path), undefined=jinja2.StrictUndefined
    )

    loaded = environment.get_template(filename)

    rendered = loaded.render(project=project)
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
        "--project_name",
        help="The name of your dbt project (as defined in dbt_project.yml). Defaults to <my_client>",
    )
    parser.add_argument(
        "--project_directory",
        help="The name of your dbt project directory. Defaults to <my-client>-dbt",
    )
    parser.add_argument(
        "--profile_name",
        help="The name of the profile your dbt project will use. Defaults to <my_client>",
    )
    parser.add_argument(
        "target_dir",
        help="The target directory name. Note that the project will be created as a subdirectory within the target directory",
    )

    parsed = parser.parse_args(args)
    return parsed


def handle(parsed):
    """ Checks that the arguments are valid, and returns a dictionary that
    describes the dbt project
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

    kebab_case_client = parsed.client.replace("_", "-")

    project = {}

    project["client_name"] = parsed.client
    project["warehouse"] = parsed.warehouse
    project["name"] = parsed.project_name or parsed.client
    project["dir_path"] = parsed.target_dir
    project["dir_name"] = parsed.project_directory or "{}-dbt".format(kebab_case_client)
    project["profile_name"] = parsed.profile_name or parsed.client

    return project


def create_starter_project(project):
    # set the path we are targeting
    client_project_path = os.path.join(project["dir_path"], project["dir_name"])
    os.mkdir(client_project_path)

    # for each file in the starter project, copy a rendered version of the file
    for subdir, dirs, files in os.walk(starter_project_path):
        for file in files:
            rendered_template = render_template(subdir, file, project)
            target_dir = subdir.replace(starter_project_path, client_project_path)
            target_filepath = os.path.join(target_dir, file)
            write_file(target_filepath, rendered_template)

    print(
        "New dbt project for {} created at {}! 🎉".format(
            project["client_name"], client_project_path
        )
    )


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parsed = parse_args(args)

    project = handle(parsed)

    create_starter_project(project)


if __name__ == "__main__":
    main()
