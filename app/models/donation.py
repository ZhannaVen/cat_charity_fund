from sqlalchemy import Column, Text

from app.models.abstract import AbstractModel


class Donation(AbstractModel):
    comment = Column(Text, nullable=True)