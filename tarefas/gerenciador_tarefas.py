class GerenciadorTarefas:
  def __init__(self):
    self.tarefas = []

  def adicionar_tarefa(self, titulo, descricao, prioridade):
    new = titulo, descricao, prioridade
    self.tarefas.append(new)
    return new