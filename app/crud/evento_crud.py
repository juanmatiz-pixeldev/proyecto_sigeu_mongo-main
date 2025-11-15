from fastapi import HTTPException,status
from app.models.evento import EventoModel
from app.schemas.evento import EventoCrear, Evento, EventoActualizar
from beanie import PydanticObjectId
from typing import List, Dict, Any


async def crear_evento(nuevo_evento: EventoCrear) -> Evento:
    ev = EventoModel(**nuevo_evento.model_dump())
    await ev.insert()
    return Evento(id=str(ev.id), **nuevo_evento.model_dump())

async def obtener_evento_por_id(evento_id: str) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    ev = await EventoModel.get(object_id)
    if not ev:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Evento {evento_id} no encontrado")
    return Evento(id=str(ev.id), **ev.model_dump())

async def listar_eventos() -> List[Evento]:
    eventos = await EventoModel.find_all().to_list()
    return [Evento(id=str(e.id), **e.model_dump()) for e in eventos]
#podriamos dejar el listar asi primitivo o detallado, pero evento tiene muchos campos. Quiza mostrar solo algunos mas esenciales

async def actualizar_evento(evento_id: str, datos: EventoActualizar) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    ev = await EventoModel.get(object_id)
    if not ev:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Evento {evento_id} no encontrado")

    campos_actualizados = datos.model_dump(exclude_unset=True)
    for k, v in campos_actualizados.items():
        setattr(ev, k, v)
    await ev.save()
    return Evento(id=str(ev.id), **ev.model_dump())


async def eliminar_evento(evento_id: str) -> None:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    ev = await EventoModel.get(object_id)
    if not ev:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Evento {evento_id} no encontrado")
    await ev.delete()
    return None

# --- Operaciones CRUD sobre arreglos embebidos ---

async def agregar_revision(evento_id: str, revision: Dict[str, Any]) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    await EventoModel.find_one({"_id": object_id}).update({"$push": {"revisiones": revision}})
    return await obtener_evento_por_id(evento_id)

async def actualizar_revision(evento_id: str, id_revision: Any, changes: Dict[str, Any]) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    set_ops = {f"revisiones.$.{k}": v for k, v in changes.items()}
    await EventoModel.find_one({"_id": object_id, "revisiones.id_revision": id_revision}).update({"$set": set_ops})
    return await obtener_evento_por_id(evento_id)

async def agregar_aval(evento_id: str, aval: Dict[str, Any]) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    await EventoModel.find_one({"_id": object_id}).update({"$push": {"avales": aval}})
    return await obtener_evento_por_id(evento_id)

async def eliminar_aval(evento_id: str, id_aval: Any) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    await EventoModel.find_one({"_id": object_id}).update({"$pull": {"avales": {"id_aval": id_aval}}})
    return await obtener_evento_por_id(evento_id)

async def agregar_responsable(evento_id: str, responsable: Dict[str, Any]) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    await EventoModel.find_one({"_id": object_id}).update({"$push": {"responsables": responsable}})
    return await obtener_evento_por_id(evento_id)

async def eliminar_responsable(evento_id: str, usuario_id: Any) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    await EventoModel.find_one({"_id": object_id}).update({"$pull": {"responsables": {"usuario_id": usuario_id}}})
    return await obtener_evento_por_id(evento_id)

async def set_certificado_participacion(evento_id: str, certificado_meta: Dict[str, Any]) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    await EventoModel.find_one({"_id": object_id}).update({"$set": {"certificado_participacion": certificado_meta}})
    return await obtener_evento_por_id(evento_id)