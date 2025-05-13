from datetime import datetime


class Tarefa:
    _id_counter = 1 

    def __init__(self, titulo, descricao, prioridade):
        self.id = Tarefa._id_counter
        Tarefa._id_counter += 1
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.data = datetime.now()
        self.status = 'pendente'
