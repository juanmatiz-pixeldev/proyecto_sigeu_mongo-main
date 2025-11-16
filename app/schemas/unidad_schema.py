from pydantic import BaseModel, Field
from typing import Optional


class FacultadRef(BaseModel):
    id_facultad: Optional[str] = None
    nombre_facultad: Optional[str] = None


class UnidadCrear(BaseModel):
    nombre_unidad: str
    facultad: Optional[FacultadRef] = None


class Unidad(BaseModel):
    id: str = Field(..., description="ID de la unidad")
    nombre_unidad: str
    facultad: Optional[FacultadRef] = None


class UnidadActualizar(BaseModel):
    nombre_unidad: Optional[str] = None
    facultad: Optional[FacultadRef] = None
