{% if project.warehouse in ('postgres', 'redshift') %}
{% raw %}
{% macro grant_select_on_schemas(schemas, groups) %}
  {% for schema in schemas %}
    grant usage on schema {{ schema }} to group {{ groups|join(', group ') }};
    grant select on all tables in schema {{ schema }} to group {{ groups|join(', group ') }};
    alter default privileges in schema {{ schema }}
        grant select on tables to group {{ groups|join(', group ') }};
  {% endfor %}
{% endmacro %}
{% endraw %}

{% elif project.warehouse == 'snowflake' %}

{% raw %}
{% macro grant_select_on_schemas(schemas, role) %}
  {% for schema in schemas %}
    grant usage on schema {{ schema }} to role {{ role }};
    grant select on all tables in schema {{ schema }} to role {{ role }};
    grant select on all views in schema {{ schema }} to role {{ role }};
    grant select on future tables in schema {{ schema }} to role {{ role }};
    grant select on future views in schema {{ schema }} to role {{ role }};
  {% endfor %}
{% endmacro %}
{% endraw %}
{% endif %}