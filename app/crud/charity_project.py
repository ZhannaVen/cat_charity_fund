# app/crud/meeting_room.py

# Импортируем sessionmaker из файла с настройками БД.
from app.core.db import AsyncSessionLocal
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectCreate
from sqlalchemy import select
from typing import Optional


async def create_charity_project(
        new_project: CharityProjectCreate
) -> CharityProject:
    new_project_data = new_project.dict()
    db_project = CharityProject(**new_project_data)
    async with AsyncSessionLocal() as session:
        session.add(db_project)
        await session.commit()
        await session.refresh(db_project)
    return db_project


async def get_project_id_by_name(charity_project: str) -> Optional[int]:
    async with AsyncSessionLocal() as session:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == charity_project
            )
        )
        db_project_id = db_project_id.scalars().first()
    return db_project_id




