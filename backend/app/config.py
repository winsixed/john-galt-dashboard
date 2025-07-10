from pydantic import BaseSettings, PostgresDsn, AnyHttpUrl
from typing import List

class Settings(BaseSettings):
    POSTGRESQL_HOST: str
    POSTGRESQL_PORT: int
    POSTGRESQL_USER: str
    POSTGRESQL_PASSWORD: str
    POSTGRESQL_DBNAME: str

    DATABASE_URL: PostgresDsn
    REDIS_URL: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"

    BOT_TOKEN: str

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl]
    RATE_LIMIT: str

    class Config:
        env_file = "../.env"
