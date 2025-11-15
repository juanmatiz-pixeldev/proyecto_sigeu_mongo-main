from beanie import Document, PydanticObjectId
from typing import Optional, List
from datetime import datetime


class UnidadAcademicaModel(Document):
    id: Optional[PydanticObjectId] = None
    nombre_unidad: str
    codigo_unidad: Optional[str] = None
    facultad: str  # Referencia a facultad
    programas_academicos: Optional[List[str]] = []  # Lista de referencias a programas
    director: Optional[str] = None  # Nombre o ID del director
    descripcion: Optional[str] = None
    estado: str = "activo"  # activo, inactivo, suspendido
    fecha_creacion: datetime = datetime.now()
    fecha_actualizacion: datetime = datetime.now()

    class Settings:
        name = "unidades_academicas"
