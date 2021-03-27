import os


def remove___main__():
    os.remove(os.path.join("{{ cookiecutter.package_name}}", "__main__.py"))


def main():
    if "{{ cookiecutter.run_server }}" == "CLI":
        remove___main__()


if __name__ == "__main__":
    main()
