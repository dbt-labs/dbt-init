# dbt-init
A cookiecutter template to create dbt projects for consulting.
dbt-init will create a project as a subdirectory within the target directory you
provide it, and populate as much of the dbt project as possible

## Usage
1. Install [cookiecutter](https://github.com/cookiecutter/cookiecutter) (preferably in a virtual environemnt) `pip install cookiecutter`
2. Then run `cookiecutter gh:fishtown-analytics/dbt-init`. This will give you a number of prompts — hitting `enter` will use the default value indicated in the `[]` parentheses.

```bash
$ cookiecutter gh:fishtown-analytics/dbt-init
name [e.g. jaffle_shop]: jaffle_shop
Select warehouse:
1 - snowflake
2 - redshift
3 - bigquery
4 - postgres
Choose from 1, 2, 3, 4 [1]: 1
client_name [jaffle-shop]:
project_name [jaffle-shop-dbt]:
profile_name [jaffle_shop]:
```
3. `cd` into your newly created dbt project!

## Once you've created your project
1. Update `sample.profile.yml` to contain the correct profile details for your
client, _excluding_ the actual credentials – e.g. username and password:
 * You can often pre-fill the host and database name.
 * You may want to use an alternate connection method (e.g. OAuth) and update
 the sample file to reflect this.
2. Ensure that the users/groups/roles within a warehouse match the grant
statements in the post-run hooks (defined in `dbt_project.yml`).

## Building out the starter project
If you're interested in helping build out the starter project, here is a list of
variables you can use – a lot of them have defaults based on the client name.
```
{{ cookiecutter.name }}: The name of the project, as defined in `dbt_project.yml`, e.g. jaffle_shop.
{{ cookiecutter.warehouse }}: The warehouse that a client is using.
{{ cookiecutter.client_name }}: The name of the client, e.g. jaffle-shop.
{{ cookiecutter.project_name }}: The name of the directory this project is in, e.g. jaffle-shop-dbt (this has to be called project name for cookiecutter reasons)
{{ cookiecutter.profile_name }}: The name of the profile used by this project, e.g. jaffle_shop.
```

## To-do:
- [ ] Configure a new profile as part of init process
