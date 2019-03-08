{% if project.warehouse == 'redshift' %}
{% raw %}
{{
    config({
        "materialized" : 'incremental',
        "post-hook" : [
          after_commit("{{ vacuum( var('maintenance', false) ) }}"),
          after_commit("{{ analyze( var('maintenance', false) ) }}")
         ]
    })
}}

select
    current_timestamp as run_at,
    {{var('maintenance', false)}} as maintenance_jobs_run
{% endraw %}
{% endif %}
