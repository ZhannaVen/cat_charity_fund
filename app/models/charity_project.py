from sqlalchemy import Column, String, Text

from .abstract import AbstractModel


class CharityProject(AbstractModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return (
            f'Проект `{self.name}`. {super().__repr__()}'
        )