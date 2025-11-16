from beanie import Document, PydanticObjectId
from typing import Optional, List
from datetime import date
from app.models.contactoemergencia import ContactoEmergencia

class PacienteModel(Document):
    id: Optional[PydanticObjectId] = None
    nombre: str
    fecha_nacimiento: date
    contactos_emergencia: Optional[List[ContactoEmergencia]] = []

    class Settings:
        name = "pacientes"
        
