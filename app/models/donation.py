from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.abstract import AbstractModel


class Donation(AbstractModel):
    comment = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"))

    def __repr__(self):
        return (
            f'Донат от {self.user_id}. {super().__repr__()}'
        )