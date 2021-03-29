"""
{% if cookiecutter.add_docker_compose == "True" and cookiecutter.add_docker == "False" %}
    '{{ cookiecutter.update({"add_docker": "True"}) }}'
{% endif %}
"""
