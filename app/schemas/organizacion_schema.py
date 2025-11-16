from pydantic import BaseModel, Field
from typing import Optional


class OrganizacionCrear(BaseModel):
    nombre_organizacion: str
    representante_legal: str
    telefono: str
    direccion: str
    actividad: str
    sector_economico: str


class Organizacion(BaseModel):
    id: str = Field(..., description="ID de la organización")
    nombre_organizacion: str
    representante_legal: str
    telefono: str
    direccion: str
    actividad: str
    sector_economico: str


class OrganizacionActualizar(BaseModel):
    nombre_organizacion: Optional[str] = None
    representante_legal: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    actividad: Optional[str] = None
    sector_economico: Optional[str] = None
