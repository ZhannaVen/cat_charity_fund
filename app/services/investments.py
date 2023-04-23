from datetime import datetime
from typing import List, Union

from app.models import Donation, CharityProject


def distribution_of_investments(
    target: Union[CharityProject, Donation],
    sources: List[Union[CharityProject, Donation]],
) -> List[Union[CharityProject, Donation]]:
    if target.invested_amount is None:
        target.invested_amount = 0
    changed_sources = set()
    for source in sources:
        to_invest = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount
        )
        for changed_source in (source, target):
            changed_source.invested_amount += to_invest
            if changed_source.full_amount == changed_source.invested_amount:
                changed_source.fully_invested = True
                changed_source.close_date = datetime.now()
        changed_sources.add(source)
        if target.fully_invested is True:
            break
    return changed_sources
