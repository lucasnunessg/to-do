from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from ...gerenciador_tarefas import GerenciadorTarefas

router = APIRouter(prefix="/tarefas", tags=["Tarefas"])

gerenciador = GerenciadorTarefas()

@router.post("/", status_code=status.HTTP_201_CREATED)
def criar_tarefa(titulo: str, descricao: str, prioridade: str):
  tarefa = gerenciador.adicionar_tarefa(titulo, descricao, prioridade)
  return tarefa

@router.get("/", status_code=status.HTTP_200_OK)
def listar_tarefas():
  tarefas = gerenciador.listar_tarefas()
  if not tarefas:
    return JSONResponse(
      content={"mesasge: Nenhuma tarefa encontrada."}
    )
  return tarefas

@router.get("/{id}")
def buscar_por_id(id: int):
  tarefa = gerenciador.buscar_por_id(id)
  if not tarefa:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"tarefa com id {id} não encontrada."
    )
  return tarefa