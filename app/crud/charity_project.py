from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectUpdate)

charity_project_crud = CRUDBase[
    CharityProject,
    CharityProjectCreate,
    CharityProjectUpdate
](CharityProject)
