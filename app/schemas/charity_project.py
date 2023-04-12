
from pydantic import Field, PositiveInt

from app.schemas.abstract import AbstractSchema


class CharityProjectCreate(AbstractSchema):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt