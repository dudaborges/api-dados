from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import PressureData

# define a estrutura de dado "usermessages" que será aceito e retornado. 
#entrada de dados
PressureDataInSchema = pydantic_model_creator(
    PressureData, name="PressureDataIn", exclude=["sensor_id"], exclude_readonly=True
)
#saída de dados
PressureDataOutSchema = pydantic_model_creator(
    PressureData, name="PressureData"
)