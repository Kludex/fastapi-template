import os
import shutil

import isort


def remove___main__():
    os.remove(os.path.join("{{ cookiecutter.package_name}}", "__main__.py"))


def remove_dockerfile():
    os.remove("Dockerfile")
    shutil.rmtree("scripts")


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


def remove_docs():
    shutil.rmtree("docs")


def remove_database():
    os.remove(os.path.join("{{ cookiecutter.package_name}}", "core/database.py"))
    os.remove("scripts/wait_database.py")
    shutil.rmtree("scripts/database")


def sort_files():
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                path = f"{root}/{file}"
                isort.file(path, quiet=True)


def main():
    if "{{ cookiecutter.database }}" == "None":
        remove_database()

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

    if "{{ cookiecutter.add_docs }}" == "False":
        remove_docs()

    sort_files()


if __name__ == "__main__":
    main()
