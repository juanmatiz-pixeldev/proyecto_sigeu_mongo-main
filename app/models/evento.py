from beanie import Document, PydanticObjectId
from pydantic import BaseModel
from typing import Optional, List, Any, Dict
from datetime import datetime


class Revision(BaseModel):
    id_revision: Any
    fecha: datetime
    descripcion: Optional[str] = None
    revisor: Optional[str] = None
    cambios: Optional[Dict[str, Any]] = None


class Aval(BaseModel):
    id_aval: Any
    fecha: datetime
    avalador: str
    comentarios: Optional[str] = None


class Responsable(BaseModel):
    usuario_id: Any
    nombre: str
    rol: str
    fecha_asignacion: datetime


class CertificadoParticipacion(BaseModel):
    plantilla_id: str
    fecha_generacion: datetime
    url_descarga: Optional[str] = None


class EventoModel(Document):
    id: Optional[PydanticObjectId] = None
    titulo: str
    descripcion: Optional[str] = None
    fecha_inicio: datetime
    fecha_fin: datetime
    ubicacion: Optional[str] = None
    organizador: str
    estado: str = "pendiente", "en curso", "finalizado"  # pendiente, en_curso, finalizado
    revisiones: Optional[List[Revision]] = []
    avales: Optional[List[Aval]] = []
    responsables: Optional[List[Responsable]] = []
    certificado_participacion: Optional[CertificadoParticipacion] = None
    fecha_creacion: datetime = datetime.now()
    fecha_actualizacion: datetime = datetime.now()

    class Settings:
        name = "eventos"
