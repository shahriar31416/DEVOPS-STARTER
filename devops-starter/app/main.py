from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI(title="DevOps Starter API", version="1.0.0")

# Allow your GitHub Pages frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://shahriar31416.github.io"],  # use ["*"] temporarily if needed
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    id: int
    name: str

@app.get("/", include_in_schema=False)
def root():
    return JSONResponse({"message": "DevOps Starter API. See /docs and /healthz"})

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/items")
def create_item(item: Item):
    return {"message": "created", "item": item}

