from typing import Any, Dict, Optional

from pydantic import AnyUrl, BaseSettings, SecretStr, validator


class Settings(BaseSettings):
    PROJECT_NAME: str
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


settings = Settings()
