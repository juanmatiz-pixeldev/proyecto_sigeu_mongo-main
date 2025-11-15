from beanie import Document, PydanticObjectId
from typing import Optional
from datetime import datetime


class InstalacionModel(Document):
    id: Optional[PydanticObjectId] = None
    nombre_instalacion: str
    tipo_instalacion: str
    ubicacion: str
    fecha_creacion: datetime = datetime.now()
    fecha_actualizacion: datetime = datetime.now()

    class Settings:
        name = "instalaciones"
