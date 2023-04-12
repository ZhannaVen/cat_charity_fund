# app/api/meeting_room.py

from fastapi import APIRouter, HTTPException, Depends

from app.crud.charity_project import create_charity_project
from app.schemas.charity_project import CharityProjectCreate, CharityProjectDB
from app.crud.charity_project import create_charity_project, get_project_id_by_name
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session


router = APIRouter()


@router.post(
    '/charity_project/',
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