import os


def remove___main__():
    os.remove(os.path.join("{{ cookiecutter.package_name}}", "__main__.py"))


def remove_dockerfile():
    os.remove("Dockerfile")


def remove_docker_compose():
    os.remove("docker-compose.yaml")


def remove_requirements():
    filenames = ["dev_requirements.txt", "requirements.txt"]
    for file in filenames:
        os.remove(file)


def remove_dev_requirements():
    os.remove("dev_requirements.txt")


def remove_poetry():
    os.remove("pyproject.toml")


def remove_python_client_config():
    os.remove("client-config.yaml")


def main():
    if "{{ cookiecutter.run_server }}" == "CLI":
        remove___main__()

    if "{{ cookiecutter.add_docker }}" == "False":
        remove_dockerfile()

    if "{{ cookiecutter.add_docker_compose }}" == "False":
        remove_docker_compose()

    if "{{ cookiecutter.packaging }}" == "poetry":
        remove_requirements()
    elif "{{ cookiecutter.packaging }}" == "pip":
        remove_poetry()
    else:
        remove_dev_requirements()

    if "{{ cookiecutter.add_python_client }}" == "False":
        remove_python_client_config()


if __name__ == "__main__":
    main()
