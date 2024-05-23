from fastapi import FastAPI
from src.database.register import register_tortoise 
from src.database.config import TORTOISE_ORM  
from tortoise import Tortoise
from src.routes import pressure


Tortoise.init_models(["src.database.models"], "models")  

app = FastAPI()

app.include_router(pressure.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

@app.get("/")
def home():
    return "Hello, World!"