from setuptools import setup, find_packages
from setuptools.command.install import install


package_name = "dbt-init"
VERSION = "0.2.0"
description = """Create a dbt project the way Fishtown Analytics would"""


class VerifyVersionCommand(install):
    """
    Custom command to verify that the git tag matches our version
    https://circleci.com/blog/continuously-deploying-python-packages-to-pypi-with-circleci/
    """

    description = "verify that the git tag matches our version"

    def run(self):
        tag = os.getenv("CIRCLE_TAG")

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)


setup(
    name=package_name,
    version=VERSION,
    description=description,
    author="Claire Carroll",
    author_email="claire@fishtownanalytics.com",
    url="https://github.com/fishtown-analyics/dbt-init",
    packages=find_packages(),
    package_data={},
    test_suite="test",
    entry_points={"console_scripts": ["dbt-init = core.main:main"]},
    scripts=[],
    install_requires=["jinja2"],
    cmdclass={"verify": VerifyVersionCommand},
)
