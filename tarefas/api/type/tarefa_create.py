from pydantic import BaseModel


class TarefaCreate(BaseModel):
    titulo: str
    descricao: str
    prioridade: str