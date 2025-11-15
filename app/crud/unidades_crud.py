from fastapi import HTTPException, status
from beanie import PydanticObjectId
from typing import List, Optional
from app.models.unidad import UnidadAcademicaModel
from app.schemas.unidad import UnidadCrear, Unidad, UnidadActualizar

async def crear_unidad(nuevo: UnidadCrear) -> Unidad:
    u = UnidadAcademicaModel(**nuevo.model_dump())
    await u.insert()
    return Unidad(id=str(u.id), **nuevo.model_dump())

async def obtener_unidad_por_id(unidad_id: str) -> Unidad:
    try:
        oid = PydanticObjectId(unidad_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de unidad invalido")
    u = await UnidadAcademicaModel.get(oid)
    if not u:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Unidad {unidad_id} no encontrada")
    return Unidad(id=str(u.id), **u.model_dump())

async def listar_unidades() -> List[Unidad]:
    items = await UnidadAcademicaModel.find_all().to_list()
    return [Unidad(id=str(x.id), **x.model_dump()) for x in items]

async def actualizar_unidad(unidad_id: str, datos: UnidadActualizar) -> Unidad:
    try:
        object_id = PydanticObjectId(unidad_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="id de unidad inválido")

    u = await UnidadAcademicaModel.get(object_id)
    if not u:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Unidad {unidad_id} no encontrada")
    u.nombre_unidad = datos.nombre_unidad or u.nombre_unidad
    u.facultad = datos.facultad or u.facultad
    await u.save()
    return Unidad(
        id=str(u.id),
        nombre_unidad=u.nombre_unidad,
        facultad=u.facultad,
    )

async def eliminar_unidad(unidad_id: str) -> None:
    try:
        oid = PydanticObjectId(unidad_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de unidad inválido")
    u = await UnidadAcademicaModel.get(oid)
    if not u:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Unidad {unidad_id} no encontrada")
    await u.delete()
    return None