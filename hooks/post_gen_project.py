import os


def remove___main__():
    os.remove(os.path.join("{{ cookiecutter.package_name}}", "__main__.py"))


def remove_dockerfile():
    os.remove("Dockerfile")


def remove_requirements():
    filenames = ["dev_requirements.txt", "requirements.txt"]
    for file in filenames:
        os.remove(file)


def remove_dev_requirements():
    os.remove("dev_requirements.txt")


def remove_poetry():
    os.remove("pyproject.toml")


def remove_env_file():
    os.remove(".env")


def main():
    if "{{ cookiecutter.run_server }}" == "CLI":
        remove___main__()

    if "{{ cookiecutter.docker }}" == "n":
        remove_dockerfile()

    if "{{ cookiecutter.packaging }}" == "poetry":
        remove_requirements()
    elif "{{ cookiecutter.packaging }}" == "pip":
        remove_poetry()
    else:
        remove_dev_requirements()

    remove_env_file()


if __name__ == "__main__":
    main()
