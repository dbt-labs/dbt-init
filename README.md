# dbt-init
A tool to create dbt projects for consulting.
dbt-init will create a project as a subdirectory within the target directory you
provide it, and populate as much of the dbt project as possible

## Installation & usage
1. Install using `pip install dbt-init`
2. To create a new client project run a command like following:
```bash
$ dbt-init --client jaffle_shop --warehouse snowflake --target_dir ~/clients/
```
You can also check the available arguments with `dbt-init --help`

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
{{ project.name }}: The name of the project, as defined in `dbt_project.yml`, e.g. jaffle_shop.
{{ project.warehouse }}: The warehouse that a client is using.
{{ project.client_name }}: The name of the client, e.g. jaffle_shop.
{{ project.dir_name }}: The name of the directory this project is in, e.g. jaffle-shop-dbt.
{{ project.profile_name }}: The name of the profile used by this project, e.g. jaffle_shop.
```

## To-do:
- [ ] Configure a new profile as part of init process
