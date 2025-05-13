from fastapi import FastAPI

app = FastAPI(
    title="Gerenciador de Tarefas"
)

@app.get("/")
def home():
    return {"message": "Olá Mundo!"}