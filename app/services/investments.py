from datetime import datetime
from typing import Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import false

from app.models import CharityProject, Donation


async def close_invested_object(
    object_to_close: Union[CharityProject, Donation],
) -> None:
    object_to_close.fully_invested = True
    object_to_close.close_date = datetime.now()


async def distribution_of_investments(
    object_in: Union[CharityProject, Donation],
    session: AsyncSession
):
    db_model = (
        CharityProject if isinstance(object_in, Donation) else Donation
    )
    open_objects = await session.execute(
        select(
            db_model
        ).where(
            db_model.fully_invested == false()
        ).order_by(
            db_model.create_date
        )
    )
    open_objects = open_objects.scalars().all()
    if open_objects:
        for object in open_objects:
            object_investments = object.full_amount - object.invested_amount
            object_in_investments = object_in.full_amount
            to_invest = (
                object_investments if object_investments < object_in_investments else object_in_investments
            )
            object.invested_amount += to_invest
            object_in.invested_amount += to_invest
            object_in_investments -= to_invest

            if object.full_amount == object.invested_amount:
                await close_invested_object(object)

            if not object_in_investments:
                await close_invested_object(object_in)
                break
        await session.commit()
        await session.refresh(object_in)
    return object_in