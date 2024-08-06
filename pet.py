from fastapi import FastAPI
from pydantic import BaseModel
import petdb

app = FastAPI()

db = {}

class Item(BaseModel):
    pettype: str
    name: str
    age: int
    address: str

@app.post("/")
def create(item: Item):
    db[item.name] = item
    return {"item": item}

@app.get("/")
def get_all_data():
    return db

@app.delete("/")
def delete_data(name: str):
    del db[name]
    return db

@app.put("/")
def update_data(item: Item):
    db[item.name] = item
    return db