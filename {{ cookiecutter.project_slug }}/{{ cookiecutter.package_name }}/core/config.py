from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, SecretStr, validator


class Settings(BaseSettings):
    POSTGRES_HOST: str = "host"
    POSTGRES_PORT: str = "host"
    POSTGRES_USER: str = "host"
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_DB: str = "host"
    POSTGRES_URI: Optional[PostgresDsn] = None

    @validator("POSTGRES_URI", pre=True)
    def validate_database(cls, value: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(value, str):
            return value
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD").get_secret_value(),
            host=values.get("POSTGRES_HOST"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )


settings = Settings()
