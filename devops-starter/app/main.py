from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="DevOps Starter API", version="1.0.0")

class Item(BaseModel):
    id: int
    name: str

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/items")
def create_item(item: Item):
    return {"message": "created", "item": item}
