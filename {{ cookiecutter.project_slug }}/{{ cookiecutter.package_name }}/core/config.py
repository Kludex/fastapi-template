{%- if cookiecutter.add_cors == 'True' %}
from typing import List, Union

from pydantic import BaseSettings, AnyHttpUrl, validator
{%- else -%}
from pydantic import BaseSettings
{%- endif %}


class Settings(BaseSettings):
    PROJECT_NAME: str
    {%- if cookiecutter.add_cors == 'True' %}
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    {% endif %}


settings = Settings()
