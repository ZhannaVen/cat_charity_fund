from typing import Optional

from pydantic import BaseModel, BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'QRKot'
    app_description: str = 'Приложение для Благотворительного фонда поддержки котиков'
    database_cat_fund: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()


class Model(BaseModel):

    class Config:
        min_anystr_length = 1
        error_msg_templates = {
            'value_error.any_str.min_length': 'min_length:{limit_value}',
        }