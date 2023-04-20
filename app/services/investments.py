from datetime import datetime
from typing import Union


from app.models import CharityProject, Donation


def close_invested_object(
    object_to_close: Union[CharityProject, Donation],
) -> None:
    object_to_close.fully_invested = True
    object_to_close.close_date = datetime.now()


def distribution_of_investments(
    object_in: Union[CharityProject, Donation],
    open_objects,

):
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
            close_invested_object(object)

        if not object_in_investments:
            close_invested_object(object_in)
            break
    return object_in, open_objects