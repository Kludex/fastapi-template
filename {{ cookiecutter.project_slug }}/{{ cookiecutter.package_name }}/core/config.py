from pydantic import BaseSettings
{%- if cookiecutter.add_cors == 'True' %}
from typing import List, Union

from pydantic import BaseSettings, AnyHttpUrl, validator
{%- endif %}
{%- if cookiecutter.database == "PostgreSQL" %}
from typing import Any, Dict, Optional

from pydantic import BaseSettings, AnyUrl, SecretStr, validator
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
    {%- if cookiecutter.database == 'PostgreSQL' %}
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_DB: str
    POSTGRES_URI: Optional[AnyUrl] = None

    @validator("POSTGRES_URI", pre=True)
    def postgres_conn(cls, value: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(value, str):
            return value
        password: SecretStr = values.get("POSTGRES_PASSWORD")
        return AnyUrl.build(
            scheme="postgresql+asyncpg",
            host=values.get("POSTGRES_HOST"),
            port=values.get("POSTGRES_PORT"),
            user=values.get("POSTGRES_USER"),
            password=password.get_secret_value(),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )
    {%- endif %}


settings = Settings()
