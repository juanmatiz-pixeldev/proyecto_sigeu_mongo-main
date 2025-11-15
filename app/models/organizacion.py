from beanie import Document, PydanticObjectId
from typing import Optional
from datetime import datetime


class OrganizacionExternaModel(Document):
    id: Optional[PydanticObjectId] = None
    nombre_organizacion: str
    representante_legal: str
    telefono: str
    direccion: str
    actividad: str
    sector_economico: str
    fecha_creacion: datetime = datetime.now()
    fecha_actualizacion: datetime = datetime.now()

    class Settings:
        name = "organizaciones_externas"
