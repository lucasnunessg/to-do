from tarefas.gerenciador_tarefas import GerenciadorTarefas

gerenciador = GerenciadorTarefas()

gerenciador.adicionar_tarefa("Estudar python", "preciso estudar fast API", "alta")


tarefas = gerenciador.listar_tarefas()
if not tarefas:  
    print("Não há tarefas para serem mostradas.")
else:
    for tarefa in tarefas:
        print(f"id: {tarefa.id}, Título: {tarefa.titulo}, status: {tarefa.status}")


tarefa_deletada = gerenciador.buscar_por_id(1)
if tarefa_deletada:
  print(f"Tarefa {tarefa_deletada.titulo} deletada com sucesso!")
  gerenciador.apagar_tarefa(1)
else:
  print(f"Tarefa não encontrada")


tarefas = gerenciador.listar_tarefas()
if not tarefas:  
    print("Não há tarefas para serem mostradas.")
else:
    for tarefa in tarefas:
        print(f"id: {tarefa.id}, Título: {tarefa.titulo}, status: {tarefa.status}")


gerenciador.adicionar_tarefa("Estudar python", "preciso estudar fast API", "alta")
tarefas = gerenciador.listar_tarefas()
for tarefa in tarefas:
 print(f"id: {tarefa.id}, Título: {tarefa.titulo}, status: {tarefa.status}" )

tarefa_editada = gerenciador.buscar_por_id(2)
if tarefa_editada:
  gerenciador.editar_tarefa(2, "Estudar Java", "pra melhorar como dev", "alta")
else:
  "Tarefa não encontrada"

tarefas = gerenciador.listar_tarefas()
if not tarefas:  
    print("Não há tarefas para serem mostradas.")
else:
    for tarefa in tarefas:
        print(f"id: {tarefa.id}, Título: {tarefa.titulo}, status: {tarefa.status}")
