
from pydantic import BaseModel, Extra, Field, PositiveInt, validator

from app.schemas.abstract import AbstractSchema

INVALID_VALUE = 'Поле не может быть пустым!'


class Model(BaseModel):
    class Config:
        min_anystr_length = 1
        error_msg_templates = {
            'value_error.any_str.min_length': 'min_length:{limit_value}',
        }


class CharityProjectCreate(Model):
    name: str = Field(..., max_length=100)
    description: str = Field(...)
    full_amount: PositiveInt = Field(..., example=1000)


class CharityProjectDB(CharityProjectCreate, AbstractSchema):
    id: int

    class Config:
        orm_mode = True


class CharityProjectUpdate(Model):
    name: str = Field(None, max_length=100)
    description: str = Field(None)
    full_amount: PositiveInt = Field(None)

    class Config:
        extra = Extra.forbid

    @validator('name', 'description')
    def value_cannot_be_null(cls, value):
        if value is None:
            raise ValueError(INVALID_VALUE)
        return value