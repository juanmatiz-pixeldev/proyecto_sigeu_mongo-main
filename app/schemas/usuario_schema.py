from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Any
from datetime import datetime


class Estudiante(BaseModel):
    programa_id: Optional[Any] = None
    nombre_programa: Optional[str] = None


class Docente(BaseModel):
    unidad_id: Optional[Any] = None
    nombre_unidad: Optional[str] = None


class Contrasena(BaseModel):
    id_contrasena: Optional[Any] = None
    fecha_creacion: Optional[datetime] = None
    fecha_ultimo_cambio: Optional[datetime] = None
    vigente: Optional[bool] = True


class Notificacion(BaseModel):
    id_notificacion: Optional[Any] = None
    evento_id: Optional[Any] = None
    mensaje: Optional[str] = None
    fecha: Optional[datetime] = None


class UsuarioCrear(BaseModel):
    nombre: str
    correo: EmailStr
    telefono: Optional[str] = None
    rol_usuario: str
    perfil: Optional[str] = None
    estudiante: Optional[Estudiante] = None
    docente: Optional[Docente] = None


class UsuarioActualizar(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = None
    rol_usuario: Optional[str] = None
    perfil: Optional[str] = None
    estudiante: Optional[Estudiante] = None
    docente: Optional[Docente] = None


class Usuario(UsuarioCrear):
    id: str = Field(..., description="ID del usuario")
    contrasenas: Optional[List[Contrasena]] = []
    notificaciones: Optional[List[Notificacion]] = []
