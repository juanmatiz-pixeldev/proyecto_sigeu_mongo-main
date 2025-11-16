from beanie import Document, PydanticObjectId
from pydantic import BaseModel
from typing import Optional


class Facultad(BaseModel):
    id_facultad: Optional[str] = None
    nombre_facultad: Optional[str] = None


class ProgramaModel(Document):
    id: Optional[PydanticObjectId] = None
    nombre_programa: str
    facultad: Optional[Facultad] = None

    class Settings:
        name = "programas"
