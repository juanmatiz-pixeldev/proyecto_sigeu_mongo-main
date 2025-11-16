from beanie import Document, PydanticObjectId
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime


class Estudiante(BaseModel):
    programa_id: Optional[str] = None
    nombre_programa: Optional[str] = None


class Docente(BaseModel):
    unidad_id: Optional[str] = None
    nombre_unidad: Optional[str] = None


class Contrasena(BaseModel):
    id_contrasena: Optional[str] = None
    fecha_creacion: datetime
    fecha_ultimo_cambio: datetime
    vigente: bool


class Notificacion(BaseModel):
    id_notificacion: Optional[str] = None
    evento_id: Optional[str] = None
    mensaje: Optional[str] = None
    fecha: datetime


class UsuarioModel(Document):
    id: Optional[PydanticObjectId] = None
    nombre: str
    correo: EmailStr
    telefono: Optional[str] = None
    rol_usuario: str
    perfil: Optional[str] = None
    estudiante: Optional[Estudiante] = None
    docente: Optional[Docente] = None
    contrasenas: Optional[List[Contrasena]] = []
    notificaciones: Optional[List[Notificacion]] = []

    class Settings:
        name = "usuarios"
