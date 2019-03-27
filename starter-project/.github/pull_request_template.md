<!--- Provide a short summary in the Title above -->
<!--- Examples of good PR titles: "Feature: add so-and-so models"; "Fix: deduplicate such-and-such"; "Update: dbt version 0.13.0" -->

## Notes/Limitations/Next Steps
<!--- Describe your changes in detail including any potential issues. -->
<!--- Is this linked to an open issue or another pull request? Link it here. -->

## Screenshots (if appropriate):
<!--- Include a screenshot of the relevant section of the updated DAG, if this PR adds or removes models. You can access your version of the DAG by running `dbt docs generate && dbt docs serve`.  -->

## Checklist:
<!--- Go over all the following points, and put an `x` in all the boxes that apply. -->
<!--- Remove any boxes that are not relevant -->

<!---General dbt -->
- [ ] My models are materialized appropriately.
- [ ] My commits are related to the pull request and look clean. 
- [ ] My SQL follows the [Fishtown Analytics style guide](https://github.com/fishtown-analytics/corp/blob/master/dbt_coding_conventions.md).
- [ ] My new models have the appropriate tests and documentation in my yml files.
- [ ] I have update the README file.

<!---Redshift Specifc -->
- [ ] Sort and dist keys have been added to models materialized as tables.
- [ ] I have tested the downstream models from my late binding views. 

<!---Snowflake Specifc -->

<!---BigQuery Specifc -->