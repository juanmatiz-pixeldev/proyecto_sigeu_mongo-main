from pydantic import BaseModel
from enum import Enum

class RelacionEnum(str, Enum):
    PADRE = "padre"
    MADRE = "madre"
    HERMANO = "hermano"
    OTRO = "otro"

class ContactoEmergencia(BaseModel):
    nombre: str
    relacion: RelacionEnum
    telefono: int
