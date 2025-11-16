from beanie import Document, PydanticObjectId
from typing import Optional

class FacultadModel(Document):
    id: Optional[PydanticObjectId] = None
    nombre_facultad: str

    class Settings:
        name = "facultades"
