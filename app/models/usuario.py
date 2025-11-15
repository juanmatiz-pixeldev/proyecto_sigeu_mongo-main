from beanie import Document, PydanticObjectId
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime


class PasswordHistory(BaseModel):
    password: str
    fechaCambio: datetime = datetime.now()


class UsuarioModel(Document):
    id: Optional[PydanticObjectId] = None
    nombre: str
    correo: EmailStr
    rol: str
    passwordActual: str
    historialPasswords: List[PasswordHistory] = []
    estado: str = "activo"
    fecha_creacion: datetime = datetime.now()
    fecha_actualizacion: datetime = datetime.now()

    class Settings:
        name = "usuarios"
