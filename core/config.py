from dotenv import find_dotenv
from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    pg_dsn: PostgresDsn

    class Config:
        env_file = find_dotenv(".env")


settings = Settings()
