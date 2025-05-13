from tarefas.tarefas_main import Tarefa


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
  
  def editar_tarefa(self, id, novo_titulo=None, nova_descricao= None, nova_prioridade= None):
    tarefa_editada = self.buscar_por_id(id)
    if tarefa_editada:
      if novo_titulo is not None:
        tarefa_editada.titulo = novo_titulo
        if nova_descricao is not None:
          tarefa_editada.descricao = nova_descricao
          if nova_prioridade is not None:
            tarefa_editada.prioridade = nova_prioridade
            return True
          return False        


  
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
      
  
