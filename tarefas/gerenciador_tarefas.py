class GerenciadorTarefas:
  def __init__(self):
    self.tarefas = []

  def adicionar_tarefa(self, titulo, descricao, prioridade):
    new = titulo, descricao, prioridade
    self.tarefas.append(new)
    return new
  
  def listar_tarefas(self):
    return self.tarefas
  
  def buscar_por_id(self, id):
    for tarefa in self.tarefas:
      if tarefa.id == id:
        return tarefa
      return None
  
  def apagar_tarefa(self):
    delete = self.tarefas.remove()
    return delete