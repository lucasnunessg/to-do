from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from tarefas.api.type.tarefa_create import TarefaCreate
from ...gerenciador_tarefas import GerenciadorTarefas

router = APIRouter(prefix="/tarefas", tags=["Tarefas"])

gerenciador = GerenciadorTarefas()

@router.post("/adicionar", status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa_data: TarefaCreate):
  tarefa = gerenciador.adicionar_tarefa(titulo=tarefa_data.titulo, 
                                        descricao=tarefa_data.descricao,
                                        prioridade=tarefa_data.prioridade)
  return tarefa.__dict__

@router.get("/", status_code=status.HTTP_200_OK)
def listar_tarefas():
  tarefas = gerenciador.listar_tarefas()
  if not tarefas:
    return JSONResponse(
    content={"message": "Nenhuma tarefa encontrada."}
    )
  if isinstance(tarefas, set):
    return list(tarefas)
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

@router.put("/{id}")
def editar_tarefa(id: int):
  tarefa = gerenciador.buscar_por_id(id)
  if not tarefa:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"tarefa {id} não encontrada."
    )
  gerenciador.editar_tarefa(tarefa)
  return tarefa