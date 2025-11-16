from pydantic import BaseModel, Field
from typing import Optional


class FacultadRef(BaseModel):
    id_facultad: Optional[str] = None
    nombre_facultad: Optional[str] = None


class ProgramaCrear(BaseModel):
    nombre_programa: str
    facultad: Optional[FacultadRef] = None


class Programa(BaseModel):
    id: str = Field(..., description="ID del programa")
    nombre_programa: str
    facultad: Optional[FacultadRef] = None


class ProgramaActualizar(BaseModel):
    nombre_programa: Optional[str] = None
    facultad: Optional[FacultadRef] = None
