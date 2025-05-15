from fastapi import FastAPI
from .endpoints.api_endpoints import router as tarefas_router

app = FastAPI(
    title="Gerenciador de Tarefas"
)

app.include_router(tarefas_router)

@app.get("/")
def home():
    return {"message": "api para gerenciamento de tarefas"}