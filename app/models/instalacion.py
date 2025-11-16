from beanie import Document, PydanticObjectId
from typing import Optional


class InstalacionModel(Document):
    id: Optional[PydanticObjectId] = None
    nombre_instalacion: str
    ubicacion: str
    tipo_instalacion: str

    class Settings:
        name = "instalaciones"
