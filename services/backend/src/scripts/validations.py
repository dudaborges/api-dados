from src.crud.data_iot import get_data_iot

async def compare_pressure_data(data_array):
    # como pegar o penúltimo dado da api e comparar com o atual? substituir nesse código
    current_pressure_data = data_array[-1]['pressure']
    previous_pressure_data = data_array[-2]['pressure']
    pressure_change_limit = 5

    diferenca_dos_dados = await abs(current_pressure_data - previous_pressure_data)

    if diferenca_dos_dados > pressure_change_limit:
        return f'[ALERTA] A pressão aumentou repentinamente! De {previous_pressure_data}hPa foi para {current_pressure_data}hPa em 5 minutos'
    else:
        return 'Pressão estável.'

async def compare_temperature_data(data_array):
    current_temperature_data = data_array['temperature']
    previous_temperature_data = x
    temperature_change_limit = 5

    diferenca_dos_dados = await abs(current_temperature_data - previous_temperature_data)

    if diferenca_dos_dados > temperature_change_limit:
        return f'[ALERTA] A temperatura aumentou repentinamente! De {previous_temperature_data}°C foi para {current_temperature_data}°C em 5 minutos'
    else:
        return 'Temperatura estável.'
    


async def check_data_within_range(data_array):
    current_pressure = data_array['pressure']
    current_temperature = data_array['temperature']

    data_iot = await get_data_iot()
    print('DATA IOT: ', data_iot)
# ver quais intervalos botar
    if not (1000 <= current_pressure <= 10020):
        return f'[ALERTA] Pressão fora do intervalo! Pressão atual: {current_pressure}hPa'
    if not (27 <= current_temperature <= 35):
        return f'[ALERTA] Temperatura fora do intervalo! Temperatura atual: {current_temperature}°C'

    return 'Dados dentro do intervalo esperado.'
