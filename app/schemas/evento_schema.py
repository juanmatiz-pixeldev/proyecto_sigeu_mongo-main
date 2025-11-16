from pydantic import BaseModel, Field
from typing import Optional, List, Any
from datetime import datetime


class OrganizacionRef(BaseModel):
    id_organizacion: Optional[Any] = None
    nombre_organizacion: Optional[str] = None


class InstalacionRef(BaseModel):
    id_instalacion: Optional[Any] = None
    nombre_instalacion: Optional[str] = None
    ubicacion: Optional[str] = None
    tipo_instalacion: Optional[str] = None


class Revision(BaseModel):
    id_revision: Optional[Any] = None
    estado: Optional[str] = None
    fecha_revision: Optional[datetime] = None
    justificacion: Optional[str] = None
    secretario: Optional[dict] = None


class Aval(BaseModel):
    id_aval: Optional[Any] = None
    fecha_emision: Optional[datetime] = None
    emitido_por: Optional[str] = None
    rol_responsable: Optional[str] = None


class Responsable(BaseModel):
    usuario_id: Optional[Any] = None
    nombre_responsable: Optional[str] = None


class CertificadoParticipacion(BaseModel):
    id_certificado: Optional[Any] = None
    organizacion_id: Optional[Any] = None
    representante: Optional[str] = None
    fecha_emision: Optional[datetime] = None


class EventoCrear(BaseModel):
    titulo: str
    fecha_inicio: datetime
    fecha_fin: datetime
    publicado: Optional[bool] = False
    organizacion: Optional[OrganizacionRef] = None
    instalacion: Optional[InstalacionRef] = None
    unidad: Optional[Any] = None


class EventoActualizar(BaseModel):
    titulo: Optional[str] = None
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None
    publicado: Optional[bool] = None
    organizacion: Optional[OrganizacionRef] = None
    instalacion: Optional[InstalacionRef] = None
    unidad: Optional[Any] = None


class Evento(EventoCrear):
    id: str = Field(..., description="ID del evento")
    revisiones: Optional[List[Revision]] = []
    avales: Optional[List[Aval]] = []
    responsables: Optional[List[Responsable]] = []
    certificado_participacion: Optional[CertificadoParticipacion] = None
