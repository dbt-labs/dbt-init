# dbt-init
A tool to create dbt projects for consulting.
dbt-init will create a project as a subdirectory within the target directory you provide it.

## Installation

## Usage
Example:
```bash
$ python dbt-init.py --client jaffle_shop --warehouse snowflake  path/to/my/dbt/project
```

## Building out the starter project
If you're interested in helping build out the starter project, here is a list of variables you can use in your Jinja. Note that a lot of them have defaults based on the client name.
```
{{project.name}}: The name of the project, as defined in `dbt_project.yml`, e.g. jaffle_shop.
{{project.warehouse}}: The warehouse that a client is using (optional).
{{project.client_name}}: The name of the client, e.g. jaffle_shop.
{{project.dir_name}}: The name of the directory this project is in, e.g. jaffle-shop-dbt.
{{project.profile_name}}: The name of the profile used by this project, e.g. jaffle_shop.
```

## To-do:
- [ ] Update `starter-project` to reflect our views on modeling
- [ ] Configure a new profile as part of init process