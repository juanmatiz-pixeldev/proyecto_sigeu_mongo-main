from beanie import Document, PydanticObjectId
from typing import Optional


class OrganizacionExternaModel(Document):
    id: Optional[PydanticObjectId] = None
    nombre_organizacion: str
    representante_legal: str
    telefono: str
    direccion: str
    actividad: str
    sector_economico: str

    class Settings:
        name = "organizaciones_externas"
