from tarefas.gerenciador_tarefas import GerenciadorTarefas, TarefasUpdateAttrs

gerenciador = GerenciadorTarefas()

gerenciador.adicionar_tarefa("Estudar python", "preciso estudar fast API", "alta")

print("\nTarefas iniciais:")
tarefas = gerenciador.listar_tarefas()
if not tarefas:  
    print("Não há tarefas para serem mostradas.")
else:
    for tarefa in tarefas:
        print(f"id: {tarefa.id}, Título: {tarefa.titulo}, status: {tarefa.status}")

print("\nTentando deletar tarefa 1:")
tarefa_deletada = gerenciador.buscar_por_id(1)
if tarefa_deletada:
    print(f"Tarefa {tarefa_deletada.titulo} deletada com sucesso!")
    gerenciador.apagar_tarefa(1)
else:
    print("Tarefa não encontrada")

print("\nApós deletar:")
tarefas = gerenciador.listar_tarefas()
if not tarefas:  
    print("Não há tarefas para serem mostradas.")
else:
    for tarefa in tarefas:
        print(f"id: {tarefa.id}, Título: {tarefa.titulo}, status: {tarefa.status}")

gerenciador.adicionar_tarefa("Estudar Python", "Aprender Djangoo", "média")

print("\nEditando tarefa 2:")
tarefa_editada = gerenciador.buscar_por_id(2)
if tarefa_editada:
    novos_valores = TarefasUpdateAttrs(
        titulo="Estudar Java",
        descricao="pra melhorar como dev",
        prioridade="alta"
    )
    if gerenciador.editar_tarefa(2, novos_valores):
        print("Tarefa editada com sucesso!")
    else:
        print("Falha ao editar tarefa")
else:
    print("Tarefa não encontrada")

print("\nLista final:")
tarefas = gerenciador.listar_tarefas()
if not tarefas:  
    print("Não há tarefas para serem mostradas.")
else:
    for tarefa in tarefas:
        print(f"id: {tarefa.id}, Título: {tarefa.titulo}, status: {tarefa.status}")