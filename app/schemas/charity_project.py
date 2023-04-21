
from pydantic import BaseModel, Extra, Field, PositiveInt, validator

from app.schemas.abstract import AbstractSchema
from app.core.config import Model


INVALID_VALUE = 'Поле не может быть пустым!'


class CharityProjectCreate(Model):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt = Field(..., example=1000)


class CharityProjectDB(CharityProjectCreate, AbstractSchema):
    id: int

    class Config:
        orm_mode = True


class CharityProjectUpdate(Model):
    name: str = Field(None, max_length=100)
    description: str = Field(None, min_length=1)
    full_amount: PositiveInt = Field(None)

    class Config:
        extra = Extra.forbid

    @validator('name', 'description')
    def value_cannot_be_null(cls, value):
        if value is None:
            raise ValueError(INVALID_VALUE)
        return value