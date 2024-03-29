from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import CharityProject, User
from app.schemas.donation import AllDonations, DonationBase, DonationDB
from app.services.investments import distribution_of_investments

router = APIRouter()


@router.get(
    "/",
    response_model_exclude_none=True,
    response_model=list[AllDonations],
    dependencies=[Depends(current_superuser)],
)
async def get_all_donation(session: AsyncSession = Depends(get_async_session)):
    return await donation_crud.get_multi(session)


@router.post(
    "/",
    response_model_exclude_none=True,
    response_model=DonationDB,
)
async def create_donation(
    donation: DonationBase,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    new_donation = await donation_crud.create(donation, session, user, commit=False)
    session.add_all(
        distribution_of_investments(
            new_donation,
            await donation_crud.get_underinvested_objects(
                CharityProject,
                session
            )
        )
    )
    await session.commit()
    await session.refresh(new_donation)
    return new_donation


@router.get("/my", response_model=list[DonationDB])
async def get_user_donations(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    return await donation_crud.get_user_donations(user, session)