
from pydantic import Field, PositiveInt, BaseModel

from app.schemas.abstract import AbstractSchema


class CharityProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt


class CharityProjectDB(CharityProjectCreate, AbstractSchema):
    id: int

    class Config:
        orm_mode = True