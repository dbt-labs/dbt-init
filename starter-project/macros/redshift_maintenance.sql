{% if project.warehouse == 'redshift' %}
{% raw %}
{% macro vacuum(run) %}
    {% if run == true %}
        vacuum
    {% else %}
        select 1 as test
    {% endif %}
{% endmacro %}

{% macro analyze(run) %}
    {% if run == true %}
        analyze
    {% else %}
        select 1 as test
    {% endif %}
{% endmacro %}
{% endraw %}
{% endif %}