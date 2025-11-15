from fastapi import HTTPException, status
from beanie import PydanticObjectId
from typing import List
from app.models.facultad import FacultadModel
from app.schemas.facultad import FacultadCrear, Facultad, FacultadActualizar

async def crear_facultad(nuevo: FacultadCrear) -> Facultad:
    f = FacultadModel(**nuevo.model_dump())
    await f.insert()
    return Facultad(id=str(f.id), **nuevo.model_dump())

async def obtener_facultad_por_id(fac_id: str) -> Facultad:
    try:
        oid = PydanticObjectId(fac_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de facultad inválido")
    f = await FacultadModel.get(oid)
    if not f:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Facultad {fac_id} no encontrada")
    return Facultad(id=str(f.id), **f.model_dump())

async def listar_facultades() -> List[Facultad]:
    items = await FacultadModel.find_all().to_list()
    return [Facultad(id=str(x.id), **x.model_dump()) for x in items]

async def actualizar_facultad(fac_id: str, datos: FacultadActualizar) -> Facultad:
    try:
        oid = PydanticObjectId(fac_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="id de facultad inválido"
        )

    f = await FacultadModel.get(oid)
    if not f:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Facultad {fac_id} no encontrada")

    f.nombre_facultad = datos.nombre_facultad or f.nombre_facultad

    await f.save()

    return Facultad(
        id=str(f.id),
        nombre_facultad=f.nombre_facultad,
    )

async def eliminar_facultad(fac_id: str) -> None:
    try:
        oid = PydanticObjectId(fac_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de facultad inválido")
    f = await FacultadModel.get(oid)
    if not f:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Facultad {fac_id} no encontrada")
    await f.delete()
    return None