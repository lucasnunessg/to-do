from fastapi import FastAPI
from .api_endpoints import router as tarefas_router
from sqlalchemy.orm import Session

app = FastAPI(
    title="Gerenciador de Tarefas"
)

app.include_router(tarefas_router)

def get_db():
    db = Session()

@app.get("/")
def home():
    return {"message": "api para gerenciamento de tarefas"}