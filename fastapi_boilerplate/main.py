import typer
from cookiecutter.exceptions import OutputDirExistsException
from cookiecutter.main import cookiecutter
from typer import Option, Typer

from fastapi_boilerplate import __version__
from fastapi_boilerplate.constants import Packaging, RunServer, YesOrNo

app = Typer()


def version_callback(value: bool):
    if value:
        typer.echo(f"FastAPI Boilerplate, version {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = Option(None, "--version", callback=version_callback, is_eager=True)
):
    ...


@app.command()
def template(
    *,
    project_name: str = "FastAPI Project",
    project_slug: str = "fastapi-project",
    package_name: str = "fastapi_project",
    description: str = "An amazing FastAPI project!",
    full_name: str = "Default Name",
    email: str = "default@email.com",
    run_server: RunServer = RunServer.CLI,
    docker: YesOrNo = YesOrNo.NO,
    packaging: Packaging = Packaging.PIP,
):
    try:
        cookiecutter(
            "https://github.com/Kludex/fastapi-template.git",
            no_input=True,
            extra_context={
                "project_name": project_name,
                "project_slug": project_slug,
                "package_name": package_name,
                "description": description,
                "full_name": full_name,
                "email": email,
                "run_server": run_server,
                "docker": docker,
                "packaging": packaging,
            },
        )
    except OutputDirExistsException:
        typer.echo(f"{project_slug} directory already exists.")
    else:
        typer.echo(f"{project_slug} created successfully!")
