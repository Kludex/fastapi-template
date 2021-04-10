"""
{% if cookiecutter.database == "PostgreSQL" %}
    '{{ cookiecutter.update({"add_docker_compose": "True"}) }}'
{% endif %}
{% if cookiecutter.add_docker_compose == "True" %}
    '{{ cookiecutter.update({"add_docker": "True"}) }}'
{% endif %}
"""
