from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import DataIot

DataIotInSchema = pydantic_model_creator(
    DataIot, name="DataIotIn", exclude=["sensor_id"], exclude_readonly=True
)

DataIotOutSchema = pydantic_model_creator(
    DataIot, name="DataIot"
)