from fastapi import HTTPException,status
from app.models.paciente import PacienteModel
from app.schemas.paciente import PacienteCrear, Paciente, PacienteActualizar
from beanie import PydanticObjectId
from typing import List, Optional

#cambios en Paciente por PacienteSalida por los cambios nuevos en el esquema
async def crear_paciente(nuevo_paciente: PacienteCrear) -> Paciente:
    paciente = PacienteModel(**nuevo_paciente.model_dump())
    await paciente.insert()
    return Paciente(id=str(paciente.id), **nuevo_paciente.model_dump())

async def obtener_paciente_por_id(paciente_id: str) -> Paciente:
    try:
        object_id = PydanticObjectId(paciente_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de paciente invalido")
    paciente = await PacienteModel.get(object_id)
    if not paciente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Paciente de id {paciente_id} no encontrado")
    return Paciente(
        id=str(paciente.id), 
        nombre=paciente.nombre, 
        fecha_nacimiento=paciente.fecha_nacimiento, 
        contactos_emergencia=paciente.contactos_emergencia or []
        )

async def listar_pacientes() -> List[Paciente]:
    pacientes = await PacienteModel.find_all().to_list()
    return [
        Paciente(
            id=str(paciente.id),
            nombre=paciente.nombre,
            fecha_nacimiento=paciente.fecha_nacimiento,
            contactos_emergencia=paciente.contactos_emergencia,
        )
        for paciente in pacientes
    ]

async def actualizar_paciente(paciente_id: str, datos_actualizados: PacienteActualizar) -> Paciente:
    try:
        object_id = PydanticObjectId(paciente_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de paciente invalido")
    paciente = await PacienteModel.get(object_id)
    if not paciente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Paciente de id {paciente_id} no encontrado")
    
    paciente.nombre = datos_actualizados.nombre or paciente.nombre
    paciente.fecha_nacimiento = datos_actualizados.fecha_nacimiento or paciente.fecha_nacimiento
    paciente.contactos_emergencia = datos_actualizados.contactos_emergencia or paciente.contactos_emergencia
    
    await paciente.save()
    
    return Paciente(
        id=str(paciente.id),
        nombre=paciente.nombre,
        fecha_nacimiento=paciente.fecha_nacimiento,
        contactos_emergencia=paciente.contactos_emergencia,
    )

async def buscar_padres_paciente(paciente_id: str) -> List[Paciente]:
    paciente = await obtener_paciente_por_id(paciente_id)
    try:
        object_id = PydanticObjectId(paciente_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"id de paciente {paciente_id} invalido")
    
    if not paciente.contactos_emergencia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente no tiene contactos de emergencia")
    #adicionamos la agregacion para filtrar los contactos de emergencia que son padre o madre
    pipeline = [
    {"$match": {"_id": object_id}},
    {
        "$project":
        {
            "_id": 0,
            "contactos_emergencia": {
            "$filter": {
                "input": "$contactos_emergencia",
                "as": "contacto",
                "cond": {
                "$in": [
                    "$$contacto.relacion",
                    ["padre", "madre"]
                ]
                    }
                }
                }
            }
        }
        ]
    resultado = await PacienteModel.aggregate(pipeline).to_list()
    if not resultado:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al procesar la consulta.")
    contactos = resultado[0].get("contactos_emergencia", [])
    return contactos