from src.database.models import DataIot
from src.schemas.data_iot import DataIotOutSchema
from fastapi import HTTPException
from src.scripts.validations import check_data_within_range


async def get_data_iot():
    return await DataIotOutSchema.from_queryset(DataIot.all())

async def create_data_iot(data_iot) -> DataIotOutSchema:
    try:
        data_iot_dict = data_iot.dict(exclude_unset=True)
        data_iot_dict['status'] = await check_data_within_range(data_iot_dict)
        data_iot_obj = await DataIot.create(**data_iot_dict)
        return await DataIotOutSchema.from_tortoise_orm(data_iot_obj)
    except Exception as e:
        error_message = f'An error occurred while creating the message. {e}'
        raise HTTPException(status_code=400, detail=error_message)