from beanie import Document, PydanticObjectId
from pydantic import BaseModel
from typing import Optional, List, Any
from datetime import datetime


class Organizacion(BaseModel):
    id_organizacion: Any
    nombre_organizacion: str


class Instalacion(BaseModel):
    id_instalacion: Any
    nombre_instalacion: str
    ubicacion: str
    tipo_instalacion: str


class Revision(BaseModel):
    id_revision: Any
    estado: str
    fecha_revision: datetime
    justificacion: str


class Aval(BaseModel):
    id_aval: Any
    fecha_emision: datetime
    emitido_por: str
    rol_responsable: str


class Responsable(BaseModel):
    usuario_id: Any
    nombre_responsable: str


class Certificado(BaseModel):
    id_certificado: Any
    organizador_id: Any
    representante: str
    fecha_emision: datetime


class Secretario(BaseModel):
    id_secretario: Any
    nombre_secretario: str
    unidad_id: Any
    nombre_unidad: str


class EventoModel(Document):
    id: Optional[PydanticObjectId] = None
    titulo: str
    fecha_creacion: datetime
    fecha_inicio: datetime
    fecha_fin: datetime
    publicado: bool = False
    organizacion: Optional[Organizacion] = None
    instalacion: Optional[Instalacion] = None
    revisiones: Optional[List[Revision]] = []
    avales: Optional[List[Aval]] = []
    responsable: Optional[List[Responsable]] = []
    unidad: Optional[Any] = None
    certificado_participacion: Optional[Certificado] = None
    secretario: Optional[Secretario] = None

    class Settings:
        name = "eventos"
