# app/api/meeting_room.py

from fastapi import APIRouter, HTTPException, Depends

from app.crud.charity_project import create_charity_project
from app.schemas.charity_project import CharityProjectCreate, CharityProjectDB
from app.crud.charity_project import create_charity_project, get_project_id_by_name, read_all_projects_from_db
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
    project_id = await get_project_id_by_name(charity_project.name, session)
    if project_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Проект с таким именем уже существует!',
        )
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