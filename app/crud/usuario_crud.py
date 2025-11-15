from fastapi import HTTPException, status
from beanie import PydanticObjectId
from typing import List, Optional
from app.models.usuario import UsuarioModel
from app.schemas.usuario import UsuarioCrear, Usuario, UsuarioActualizar

async def crear_usuario(nuevo_usuario: UsuarioCrear) -> Usuario:
    usuario = UsuarioModel(**nuevo_usuario.model_dump())
    await usuario.insert()
    return Usuario(id=str(usuario.id), **nuevo_usuario.model_dump())

async def obtener_usuario_por_id(usuario_id: str) -> Usuario:
    try:
        object_id = PydanticObjectId(usuario_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de usuario invalido")
    user = await UsuarioModel.get(object_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuario {usuario_id} no encontrado")
    return Usuario(id=str(user.id), **user.model_dump())

async def listar_usuarios() -> List[Usuario]:
    usuarios = await UsuarioModel.find_all().to_list()
    return [Usuario(id=str(u.id), **u.model_dump()) for u in usuarios]

async def actualizar_usuario(usuario_id: str, datos: UsuarioActualizar) -> Usuario:
    try:
        object_id = PydanticObjectId(usuario_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de usuario invalido")
    user = await UsuarioModel.get(object_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuario {usuario_id} no encontrado")

    updates = datos.model_dump(exclude_unset=True)
    for k, v in updates.items():
        setattr(user, k, v)
    await user.save()
    return Usuario(id=str(user.id), **user.model_dump())

async def eliminar_usuario(usuario_id: str) -> None:
    try:
        oid = PydanticObjectId(usuario_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de usuario inválido")
    user = await UsuarioModel.get(oid)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuario {usuario_id} no encontrado")
    await user.delete()
    return None