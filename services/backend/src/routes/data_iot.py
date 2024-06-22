from fastapi import APIRouter
from src.schemas.data_iot import DataIotOutSchema, DataIotInSchema
import src.crud.data_iot as crud
from typing import List

router = APIRouter()

@router.get('/data', response_model=List[DataIotOutSchema])
async def get_data_iot():
    return await crud.get_data_iot()

@router.post('/create', response_model=DataIotOutSchema)
async def create_data_iot(data_iot: DataIotInSchema):
    return await crud.create_data_iot(data_iot)