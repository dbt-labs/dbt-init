# dbt-init
A tool to create dbt projects for consulting.
dbt-init will create a project as a subdirectory within the target directory you
provide it, and populate as much of the dbt project as possible

## Installation & usage
1. Install using `pip install dbt-init`
2. To create a new client project run a command like following:
```bash
$ dbt-init --client jaffle_shop --warehouse snowflake --target-dir ~/clients/
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

## Testing out the changes
If you're just making simple changes to the starter project, testing out the
changes is optional. If you want to improve the script, or just get familiar
with virtual environments, this is a good idea!
1. Clone this repo and `cd` into it
2. Create a new virtual environment `dbt-init-dev` and activate it. Make sure
your virtual environment uses python 3.
3. Run `pip install -r requirements-dev.txt`
4. You should now have a development version of `dbt-init` installed. Test your
changes by creating a sample project and inspecting the results (I know, we
should build real tests), e.g.:
```
$ dbt-init --client test --target-dir ~/clrcrl/ --warehouse bigquery
New dbt project for test created at /Users/claire/clrcrl/test-dbt! 🎉

$ open /Users/claire/clrcrl/test-dbt
```

## To-do:
- [ ] Configure a new profile as part of init process
