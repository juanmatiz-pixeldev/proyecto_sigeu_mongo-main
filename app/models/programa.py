from beanie import Document, PydanticObjectId
from typing import Optional
from datetime import datetime


class ProgramaModel(Document):
    id: Optional[PydanticObjectId] = None
    nombre_programa: str
    facultad: str
    fecha_creacion: datetime = datetime.now()
    fecha_actualizacion: datetime = datetime.now()

    class Settings:
        name = "programas"
