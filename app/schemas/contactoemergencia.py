from pydantic import BaseModel
from app.models.contactoemergencia import RelacionEnum
# Schema embebido dentro de Paciente
class ContactoEmergenciaCrear(BaseModel):
    nombre: str
    relacion: RelacionEnum
    telefono: int