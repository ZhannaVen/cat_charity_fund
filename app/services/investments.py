from datetime import datetime
from typing import List

from app.models import AbstractModel


def distribution_of_investments(
    target: AbstractModel,
    sources: List[AbstractModel],
) -> List[AbstractModel]:
    if target.invested_amount is None:
        target.invested_amount = 0
    changed_sources = []
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
        changed_sources.append(source)
        if target.fully_invested is True:
            break
    return changed_sources
