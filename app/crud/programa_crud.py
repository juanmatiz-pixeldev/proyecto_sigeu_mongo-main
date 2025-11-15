from fastapi import HTTPException, status
from beanie import PydanticObjectId
from typing import List, Optional
from app.models.programa import ProgramaModel
from app.schemas.programa import ProgramaCrear, Programa, ProgramaActualizar

async def crear_programa(nuevo: ProgramaCrear) -> Programa:
    p = ProgramaModel(**nuevo.model_dump())
    await p.insert()
    return Programa(id=str(p.id), **nuevo.model_dump())

async def obtener_programa_por_id(programa_id: str) -> Programa:
    try:
        object_id = PydanticObjectId(programa_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de programa inválido")
    p = await ProgramaModel.get(object_id)
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Programa {programa_id} no encontrado")
    return Programa(id=str(p.id), **p.model_dump())

async def listar_programas() -> List[Programa]:
    items = await ProgramaModel.find_all().to_list()
    return [Programa(id=str(x.id), **x.model_dump()) for x in items]

async def actualizar_programa(programa_id: str, datos: ProgramaActualizar) -> Programa:
    try:
        object_id = PydanticObjectId(programa_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="id de programa inválido")

    p = await ProgramaModel.get(object_id)
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Programa {programa_id} no encontrado")

    p.nombre_programa = datos.nombre_programa or p.nombre_programa
    p.facultad = datos.facultad or p.facultad

    await p.save()

    return Programa(
        id=str(p.id),
        nombre_programa=p.nombre_programa,
        facultad=p.facultad,
    )

async def eliminar_programa(programa_id: str) -> None:
    try:
        oid = PydanticObjectId(programa_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de programa inválido")
    p = await ProgramaModel.get(oid)
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Programa {programa_id} no encontrado")
    await p.delete()
    return None
