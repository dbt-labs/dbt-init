# {{ cookiecutter.project_name }}

dbt models for {{ cookiecutter.client_name }}

## Getting started
1. Clone this github repo
2. Install dbt following [these instructions](https://docs.getdbt.com/docs/installation)
3. Ask your database administrator for a set of {{ cookiecutter.warehouse }} credentials.


{% if cookiecutter.warehouse == 'bigquery' %}
  You'll also need to connect to BigQuery using [these instructions](https://docs.getdbt.com/docs/profile-bigquery#section-oauth-authorization).

{% elif cookiecutter.warehouse in ('postgres', 'redshift') %}
  The database administrator should run the following statements from a super user account to create your account.
```sql
create user <user> with
  password '<generate_this>'
  in group transformer, reporter;
```
{% elif cookiecutter.warehouse == 'snowflake' %}
  The database administrator should run the following statements from a super user account to create your account.
```sql
create user <user>
    password = '<generate_this>'
    default_warehouse = transforming
    default_role = transformer;
```
{% endif %}
4. Copy the example profile to your `~/.dbt` folder (created when installing dbt):
```bash
$ cp ./sample.profiles.yml ~/.dbt/profiles.yml
```
5. Populate `~/.dbt/profiles.yml` with the credentials you obtained in step 3:
```bash
open ~/.dbt
```
6. Verify that you can connect to your database
```
$ dbt debug
```
7. Verify that you can run dbt
```
$ dbt run
```

## Coding conventions
This project follows Fishtown Analytics' [coding conventions](https://github.com/fishtown-analytics/corp/blob/master/dbt_coding_conventions.md) and [git guide](https://github.com/fishtown-analytics/corp/blob/master/git-guide.md).

## Understanding the structure of this project
This project follows the structure set out in [this article](https://discourse.getdbt.com/t/how-we-structure-our-dbt-projects/355).
