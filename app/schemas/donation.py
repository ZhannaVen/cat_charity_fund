from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt

from app.schemas.abstract import AbstractSchema


class DonationBase(BaseModel):
    comment: Optional[str]
    full_amount: PositiveInt


class DonationDB(DonationBase):
    id: int
    comment: Optional[str]
    create_date: datetime

    class Config:
        orm_mode = True


class AllDonations(DonationDB, AbstractSchema):
    user_id: int