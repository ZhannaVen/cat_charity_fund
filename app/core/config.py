# app/core/config.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'QRKot'
    app_description: str = 'Приложение для Благотворительного фонда поддержки котиков'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()        