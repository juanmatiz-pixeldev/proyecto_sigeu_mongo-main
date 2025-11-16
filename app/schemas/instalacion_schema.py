from pydantic import BaseModel, Field
from typing import Optional


class InstalacionCrear(BaseModel):
    nombre_instalacion: str
    ubicacion: str
    tipo_instalacion: str


class Instalacion(BaseModel):
    id: str = Field(..., description="ID de la instalación")
    nombre_instalacion: str
    ubicacion: str
    tipo_instalacion: str


class InstalacionActualizar(BaseModel):
    nombre_instalacion: Optional[str] = None
    ubicacion: Optional[str] = None
    tipo_instalacion: Optional[str] = None
