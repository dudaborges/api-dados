from src.database.models import PressureData
from src.schemas.pressure import PressureDataOutSchema
from fastapi import HTTPException


async def get_pressure():
    return await PressureDataOutSchema.from_queryset(PressureData.all())

async def create_pressure_data(pressure) -> PressureDataOutSchema:
    try:
        pressure_dict = pressure.dict(exclude_unset=True)
        pressure_obj = await PressureData.create(**pressure_dict)
        return await PressureDataOutSchema.from_tortoise_orm(pressure_obj)
    except Exception as e:
        error_message = f'An error occurred while creating the message. {e}'
        raise HTTPException(status_code=400, detail=error_message)