from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List
from datetime import date

from app.models.contactoemergencia import ContactoEmergencia


class PacienteCrear(BaseModel):
    nombre: str
    fecha_nacimiento: date
    contactos_emergencia: Optional[List[ContactoEmergencia]] = []

#lo nuevo
# Esquema base común (compartido entre entrada y salida)
class PacienteBase(BaseModel):
    nombre: str
    fecha_nacimiento: date
    contactos_emergencia: Optional[List[ContactoEmergencia]] = []


class PacienteActualizar(BaseModel):
    """Esquema para actualización parcial de pacientes."""
    nombre: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    contactos_emergencia: Optional[List[ContactoEmergencia]] = None


class Paciente(PacienteCrear):
    id: str = Field(..., description="ID único del paciente")
    
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        arbitrary_types_allowed=True
    )