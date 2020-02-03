# {{ project.dir_name }}

dbt models for {{ project.client_name }}

## Getting started
1. Clone this github repo
2. Install dbt following [these instructions](https://docs.getdbt.com/docs/installation)
3. Ask your database administrator for a set of {{ project.warehouse }} credentials.


{% if project.warehouse == 'bigquery' %}
  You'll also need to connect to BigQuery using [these instructions](https://docs.getdbt.com/docs/profile-bigquery#section-oauth-authorization).

{% elif project.warehouse in ('postgres', 'redshift') %}
  The database administrator should run the following statements from a super user account to create your account.
```sql
create user <user> with
  password '<generate_this>'
  in group transformer, reporter;
```
{% elif project.warehouse == 'snowflake' %}
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

{% if project.warehouse == 'snowflake' %}
## Granting privileges on Snowflake
To grant privileges on the entire target database, run the following [operation](https://docs.getdbt.com/docs/using-operations). Note that this operation will only need to be run once, you'll only need to re-run it if you change your target database.
```bash
$ dbt run-operation grant_select_on_database --args '{role: "reporter"}'

```

{% endif %}

## Coding conventions
This project follows Fishtown Analytics' [coding conventions](https://github.com/fishtown-analytics/corp/blob/master/dbt_coding_conventions.md) and [git guide](https://github.com/fishtown-analytics/corp/blob/master/git-guide.md).

## Understanding the structure of this project
This project follows the structure set out in [this article](https://discourse.getdbt.com/t/how-we-structure-our-dbt-projects/355).
