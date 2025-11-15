from fastapi import APIRouter, Query, Path, status
from app.crud import paciente as crud
from app.schemas.contactoemergencia import ContactoEmergenciaCrear
from app.schemas.paciente import PacienteCrear, Paciente, PacienteActualizar
from typing import List, Optional

router = APIRouter()

@router.post("/", response_model=Paciente, status_code=status.HTTP_201_CREATED)
async def crear_paciente(paciente: PacienteCrear):
    """Crear un nuevo paciente."""
    return await crud.crear_paciente(paciente)

@router.get("/{paciente_id}", response_model=Paciente, status_code=status.HTTP_200_OK)
async def obtener_paciente(paciente_id: str):
    return await crud.obtener_paciente_por_id(paciente_id)

@router.get("/", response_model=List[Paciente], status_code=status.HTTP_200_OK)
async def listar_pacientes():
    return await crud.listar_pacientes()

@router.put("/{paciente_id}", response_model=Paciente, status_code=status.HTTP_200_OK)
async def actualizar_paciente(
    paciente_id: str,
    datos_actualizados: PacienteActualizar
):
    return await crud.actualizar_paciente(paciente_id, datos_actualizados)

#consulta

@router.get("/{paciente_id}/padres", response_model=List[ContactoEmergenciaCrear], status_code=status.HTTP_200_OK)
async def obtener_padres_paciente(paciente_id: str):
    return await crud.buscar_padres_paciente(paciente_id)
