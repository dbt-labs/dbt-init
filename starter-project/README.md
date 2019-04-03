# {{ project.dir_name }}

dbt models for {{ project.client_name }}

## Getting started
1. Clone this github repo
1. Install dbt following [these instructions](https://docs.getdbt.com/docs/installation)
1. Ask your database administrator for a set of {{ project.warehouse }} credentials.

  The database administrator should run the following statements from a super user account to create your account.
{% if project.warehouse == 'bigquery' %}
{% elif project.warehouse in ('postgres', 'redshift') %}
```sql
create user <user> with
  password '<generate_this>'
  in group transformer, reporter;
```
{% elif project.warehouse == 'snowflake' %}
```sql
create user <user>
    password = '<generate_this>'
    default_warehouse = transforming
    default_role = transformer;
```
{% endif %}
1. Copy the example profile to your `~/.dbt` folder (created when installing dbt):
```bash
$ cp ./sample.profiles.yml ~/.dbt/profiles.yml
```
1. Populate `~/.dbt/profiles.yml` with your credentials:
```bash
open ~/.dbt
```
1. Verify that you can connect to dbt
```
$ dbt debug
```
1. Verify that you can run dbt
```
$ dbt run
```
