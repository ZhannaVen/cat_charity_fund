# app/api/meeting_room.py

from fastapi import APIRouter, HTTPException, Depends

from app.crud.charity_project import create_charity_project
from app.schemas.charity_project import CharityProjectCreate, CharityProjectDB, CharityProjectUpdate
from app.crud.charity_project import create_charity_project, get_project_id_by_name, read_all_projects_from_db, get_charity_project_by_id, update_charity_project
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session


router = APIRouter(
    prefix='/charity_project',
    tags=['Charity Projects']
)


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
)
async def create_new_charity_project(
        charity_project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session),
):
    await check_name_duplicate(charity_project.name, session)
    new_project = await create_charity_project(charity_project, session)
    return new_project


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_charity_projects(
        session: AsyncSession = Depends(get_async_session),
):
    all_projects = await read_all_projects_from_db(session)
    return all_projects


@router.patch(
    '/{charity_project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
)
async def partially_update_meeting_room(
        charity_project_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    charity_project = await get_charity_project_by_id(
        charity_project_id, session
    )
    if charity_project is None:
        raise HTTPException(
            status_code=404, 
            detail='Проект не найден!'
        )
    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)
    charity_project = await update_charity_project(
        charity_project, obj_in, session
    )
    return charity_project


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    project_id = await get_project_id_by_name(project_name, session)
    if project_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Проект с таким именем уже существует!',
        ) 