from src.database.models import DataIot
from src.schemas.data_iot import DataIotOutSchema
from fastapi import HTTPException


async def get_data_iot():
    datas_iot = await DataIotOutSchema.from_queryset(DataIot.all())
    return datas_iot

async def create_data_iot(data_iot) -> DataIotOutSchema:
    try:
        data_iot_dict = data_iot.dict(exclude_unset=True)
        data_iot_dict['status'] = await set_status(data_iot_dict)
        data_iot_obj = await DataIot.create(**data_iot_dict)
        return await DataIotOutSchema.from_tortoise_orm(data_iot_obj)
    except Exception as e:
        error_message = f'An error occurred while creating the message. {e}'
        raise HTTPException(status_code=400, detail=error_message)


async def compare_pressure_data(current_data_dict):
    datas_list = await get_data_iot()
    previous_pressure_data = datas_list[-1].pressure
    current_pressure_data = current_data_dict['pressure']
    pressure_change_limit = 5

    diferenca_dos_dados = abs(current_pressure_data - previous_pressure_data)

    if diferenca_dos_dados > pressure_change_limit:
        return f'[ALERTA] A pressão aumentou repentinamente! De {previous_pressure_data}hPa foi para {current_pressure_data}hPa em 5 minutos'
    else:
        return 'Pressão estável.'
    
async def compare_temperature_data(current_data_dict):
    datas_list = await get_data_iot()
    previous_temperature_data = datas_list[-1].temperature
    current_temperature_data = current_data_dict['temperature']
    temperature_change_limit = 5

    diferenca_dos_dados = abs(current_temperature_data - previous_temperature_data)

    if diferenca_dos_dados > temperature_change_limit:
        return f'[ALERTA] A temperatura aumentou repentinamente! De {previous_temperature_data}°C foi para {current_temperature_data}°C em 5 minutos'
    else:
        return 'Temperatura estável.'
    
async def check_data_within_range(current_data_dict):
    current_pressure = current_data_dict['pressure']
    current_temperature = current_data_dict['temperature']

    if not (1000 <= current_pressure <= 10020):
        return f'[ALERTA] Pressão fora do intervalo! Pressão atual: {current_pressure}hPa'
    if not (30 <= current_temperature <= 50):
        return f'[ALERTA] Temperatura fora do intervalo! Temperatura atual: {current_temperature}°C'

    return 'Dados dentro do intervalo esperado.'

async def set_status(current_data_dict):
    status_pressure = await compare_pressure_data(current_data_dict)
    status_temperature = await compare_temperature_data(current_data_dict)
    status_data_range = await check_data_within_range(current_data_dict)

    return f'{status_pressure} {status_temperature} {status_data_range}'

