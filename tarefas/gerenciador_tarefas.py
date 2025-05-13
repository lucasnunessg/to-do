from dataclasses import dataclass, asdict
from tarefas.tarefas_main import Tarefa

@dataclass
class TarefasUpdateAttrs:
  titulo: str = None
  descricao: str = None
  prioridade: str = None

class GerenciadorTarefas:
  def __init__(self):
    self.tarefas = []

  def adicionar_tarefa(self, titulo, descricao, prioridade):
    new = Tarefa(titulo, descricao, prioridade) 
    self.tarefas.append(new)
    return new
  
  def listar_tarefas(self):
    return self.tarefas
  
  def buscar_por_id(self, id):
    for tarefa in self.tarefas:
      if tarefa.id == id:
        return tarefa
    return None
  
  def editar_tarefa(self, id: int, attrs: TarefasUpdateAttrs):
    tarefa = self.buscar_por_id(id)
    if not tarefa:
         return False
            
    for attr, value in asdict(attrs).items():
            if value is not None:
                setattr(tarefa, attr, value)
    return True
    
  
  def apagar_tarefa(self, id):
    tarefa = self.buscar_por_id(id)
    if tarefa:
      self.tarefas.remove(tarefa)
      return True
    return False

  def marcar_concluida(self, id):
    tarefa = self.buscar_por_id(id)
    if tarefa:
      tarefa.status = 'concluída'
      return True
    return False  
      
  
