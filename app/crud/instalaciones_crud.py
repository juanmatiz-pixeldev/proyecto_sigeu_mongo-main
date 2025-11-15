from fastapi import HTTPException, status
from beanie import PydanticObjectId
from typing import List, Optional
from app.models.instalacion import InstalacionModel
from app.schemas.instalacion import InstalacionCrear, Instalacion, InstalacionActualizar

async def crear_instalacion(nuevo: InstalacionCrear) -> Instalacion:
    i = InstalacionModel(**nuevo.model_dump())
    await i.insert()
    return Instalacion(id=str(i.id), **nuevo.model_dump())

async def obtener_instalacion_por_id(inst_id: str) -> Instalacion:
    try:
        object_id = PydanticObjectId(inst_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de instalación inválido")
    i = await InstalacionModel.get(object_id)
    if not i:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Instalación {inst_id} no encontrada")
    return Instalacion(id=str(i.id), **i.model_dump())

async def listar_instalaciones() -> List[Instalacion]:
    items = await InstalacionModel.find_all().to_list()
    return [Instalacion(id=str(x.id), **x.model_dump()) for x in items]

async def actualizar_instalacion(inst_id: str, datos: InstalacionActualizar) -> Instalacion:
    try:
        object_id = PydanticObjectId(inst_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="id de instalación inválido")

    i = await InstalacionModel.get(object_id)
    if not i:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Instalación {inst_id} no encontrada")

    i.nombre_instalacion = datos.nombre_instalacion or i.nombre_instalacion
    i.tipo_instalacion = datos.tipo_instalacion or i.tipo_instalacion
    i.ubicacion = datos.ubicacion or i.ubicacion

    await i.save()

    return Instalacion(
        id=str(i.id),
        nombre_instalacion=i.nombre_instalacion,
        tipo_instalacion=i.tipo_instalacion,
        ubicacion=i.ubicacion,
    )

async def eliminar_instalacion(inst_id: str) -> None:
    try:
        oid = PydanticObjectId(inst_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de instalación inválido")
    i = await InstalacionModel.get(oid)
    if not i:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Instalación {inst_id} no encontrada")
    await i.delete()
    return None