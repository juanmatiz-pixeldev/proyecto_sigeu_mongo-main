from fastapi import HTTPException, status
from beanie import PydanticObjectId
from typing import List, Optional
from app.models.organizacion import OrganizacionExternaModel
from app.schemas.organizacion import OrganizacionCrear, Organizacion, OrganizacionActualizar

async def crear_organizacion(nuevo: OrganizacionCrear) -> Organizacion:
    org = OrganizacionExternaModel(**nuevo.model_dump())
    await org.insert()
    return Organizacion(id=str(org.id), **nuevo.model_dump())

async def obtener_organizacion_por_id(org_id: str) -> Organizacion:
    try:
        object_id = PydanticObjectId(org_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de organización inválido")
    org = await OrganizacionExternaModel.get(object_id)
    if not org:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Organización {org_id} no encontrada")
    return Organizacion(id=str(org.id), **org.model_dump())

async def listar_organizaciones(q: Optional[str] = None) -> List[Organizacion]:
    if q:
        items = await OrganizacionExternaModel.find(
            {"nombre_organizacion": {"$regex": q, "$options": "i"}}
        ).to_list()
    else:
        items = await OrganizacionExternaModel.find_all().to_list()

    return [
        Organizacion(
            id=str(org.id),
            nombre_organizacion=org.nombre_organizacion,
            representante_legal=org.representante_legal,
            telefono=org.telefono,
            direccion=org.direccion,
            actividad=org.actividad,
            sector_economico=org.sector_economico,
        )
        for org in items
    ]

async def actualizar_unidad(unidad_id: str, datos: UnidadActualizar) -> Unidad:
    try:
        oid = PydanticObjectId(unidad_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="id de unidad inválido"
        )

    u = await UnidadAcademicaModel.get(oid)
    if not u:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Unidad {unidad_id} no encontrada"
        )

    # Actualización campo por campo – estilo Paciente
    u.nombre_unidad = datos.nombre_unidad or u.nombre_unidad
    u.facultad = datos.facultad or u.facultad
    u.programas_academicos = datos.programas_academicos or u.programas_academicos
    u.estado = datos.estado or u.estado

    await u.save()

    return Unidad(
        id=str(u.id),
        nombre_unidad=u.nombre_unidad,
        facultad=u.facultad,
        programas_academicos=u.programas_academicos,
        estado=u.estado
    )

async def eliminar_organizacion(org_id: str) -> None:
    try:
        oid = PydanticObjectId(org_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de organización inválido")
    org = await OrganizacionExternaModel.get(oid)
    if not org:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Organización {org_id} no encontrada")
    await org.delete()
    return None