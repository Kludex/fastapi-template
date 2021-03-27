import uvicorn

if __name__ == "__main__":
    uvicorn.run("{{cookiecutter.package_name}}.main:app", host="0.0.0.0")
