from pydantic import BaseModel, Field
from typing import Optional


class FacultadCrear(BaseModel):
    nombre_facultad: str


class Facultad(BaseModel):
    id: str = Field(..., description="ID de la facultad")
    nombre_facultad: str


class FacultadActualizar(BaseModel):
    nombre_facultad: Optional[str] = None
