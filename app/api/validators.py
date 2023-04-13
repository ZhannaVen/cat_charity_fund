from fastapi import HTTPException
from http import HTTPStatus

from app.crud.charity_project import charity_project_crud
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.charity_project import CharityProject


OPENED_PROJECT = 'В проект были внесены средства, не подлежит удалению!'
CLOSED_PROJECT = 'Закрытый проект нельзя редактировать!'
PROJECT_DUPLICATE = 'Проект с таким именем уже существует!'
NOT_FOUND_ERROR = 'Проект не найден!'


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    object = await charity_project_crud.get_by_attribute('name', project_name, session)
    if object is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=PROJECT_DUPLICATE,
        )


async def check_charity_project_exists(
        charity_project_id: int,
        session: AsyncSession,
) -> CharityProject:
    charity_project = await charity_project_crud.get(
        charity_project_id, session
    )
    if charity_project is None:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail=NOT_FOUND_ERROR
        )
    return charity_project


async def check_charity_project_is_opened(
        charity_project_id: int,
        session: AsyncSession,
):
    object = await (
        charity_project_crud.get_by_attribute(
            'id', charity_project_id, session
        )
    )
    if object.invested_amount:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=OPENED_PROJECT
        )


async def check_charity_project_is_closed(
        charity_project_id: int,
        session: AsyncSession,
):
    object = await (
        charity_project_crud.get_by_attribute(
            'id', charity_project_id, session
        )
    )
    if object.close_date:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=CLOSED_PROJECT
        )