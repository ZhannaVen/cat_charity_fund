from datetime import datetime
from typing import List, Set

from app.core.db import Base


def distribution_of_investments(
    target: Base,
    sources: List[Base],
) -> Set:
    if target.invested_amount is None:
        target.invested_amount = 0
    target_investments = target.full_amount
    changed_sources = set()
    for source in sources:
        source_investments = source.full_amount - source.invested_amount
        to_invest = (
            source_investments if source_investments < target_investments else target_investments
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