from datetime import datetime as dt

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Integer

from app.core.db import Base


class AbstractModel(Base):
    __abstract__ = True

    full_amount = Column(
        Integer,
        CheckConstraint('full_amount > 0', name='full_amount_positive'),
        nullable=False
    )
    invested_amount = Column(
        Integer,
        # локально тесты проходят, на платформе - нет
        # sqlalchemy.exc.IntegrityError
        #CheckConstraint(
        #    'invested_amount <= full_amount',
        #    name='invested_less_full_amount'
        # ),
        default=0
    )
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=dt.now)
    close_date = Column(DateTime, nullable=True)

    def __repr__(self):
        return (
            f'Уже инвестировано/объем инвестиций: {self.invested_amount}/{self.full_amount}. '
        )
