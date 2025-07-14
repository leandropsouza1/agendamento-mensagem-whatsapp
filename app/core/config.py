from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"


# Instância única cacheada para reuso em todo o projeto
@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
