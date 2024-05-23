from fastapi import APIRouter
from src.schemas.pressure import PressureDataOutSchema, PressureDataInSchema
import src.crud.pressure as crud
from typing import List

router = APIRouter()

@router.get('/data', response_model=List[PressureDataOutSchema])
async def get_pessure():
    return await crud.get_pressure()

@router.post('/create', response_model=PressureDataOutSchema)
async def create_message(pressure_data: PressureDataInSchema):
    return await crud.create_pressure_data(pressure_data)