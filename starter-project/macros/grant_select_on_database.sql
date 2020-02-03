{% if project.warehouse == 'snowflake' %}
{% raw %}
{% macro grant_select_on_database(role, database=target.database) %}
    grant usage on database analytics to {{ role }};

    grant usage on all schemas in database {{ database }} to role {{ role }};
    grant usage on future schemas in database {{ database }} to role {{ role }};
    grant select on future tables in database {{ database }} to role {{ role }};
    grant select on future views in database {{ database }} to role {{ role }};

    grant select on future views in database {{ database }} to role {{ role }};
    grant select on all tables in database {{ database }} to role {{ role }};
{% endmacro %}
{% endraw %}