{% raw -%}
{% macro generate_schema_name(schema_name) -%}
    {{ generate_schema_name_for_env(schema_name) }}
{%- endmacro %}
{%- endraw %}
