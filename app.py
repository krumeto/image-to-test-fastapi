from fastapi import FastAPI
from pydantic import BaseModel, validator
import time
import asyncio

from ml import extract_keywords 

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello world again"}


@app.get("/users/{user_id}")
def read_user(user_id: int):
    """
    We accept a 'user_id' and return a json blob.
    """
    return {"user_id": user_id}


class Item(BaseModel):
    name: str
    price: float
    
    @validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError(f"Price >= 0, we got {value}")
        return value

@app.post("/items/")
def create_item(item: Item):
    return item

@app.get("/sleep_slow")
def sleep_slow():
    r = time.sleep(1)
    return {"status": "done"}

@app.get("/sleep_fast")
async def sleep_fast():
    r = await asyncio.sleep(1)
    return {'status': "done"}