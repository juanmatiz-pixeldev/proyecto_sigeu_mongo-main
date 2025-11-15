from beanie import Document, PydanticObjectId
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class FacultadModel(Document):
    id: Optional[PydanticObjectId] = None
    nombre_facultad: str
    descripcion: Optional[str] = None
    fecha_creacion: datetime = datetime.now()
    fecha_actualizacion: datetime = datetime.now()

    class Settings:
        name = "facultades"
