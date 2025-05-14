# Interface Simples para teste via terminal

from tarefas import TaskManager

tm = TaskManager()

def menu():
    print("\n=== Gerenciador de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Filtrar por prioridade")
    print("5. Tarefas atrasadas")
    print("6. Ordenar tarefas")
    print("7. Gerar relatório")
    print("0. Sair")

while True:
    menu()
    op = input("Escolha uma opção: ")

    if op == "1":
        nome = input("Nome: ")
        prioridade = input("Prioridade (baixa, média, alta): ")
        data = input("Data de entrega (YYYY-MM-DD): ")
        tm.add_task(nome, prioridade, data)
        print("Tarefa adicionada!")

    elif op == "2":
        print("\nTarefas:")
        for t in tm.list_tasks():
            print(t)

    elif op == "3":
        nome = input("Digite o nome da tarefa a concluir: ")
        tm.complete_task(nome)
        print("Tarefa concluída!")

    elif op == "4":
        prio = input("Prioridade para filtrar: ")
        filtradas = tm.filter_by_priority(prio)
        for t in filtradas:
            print(t)

    elif op == "5":
        data = input("Data atual (YYYY-MM-DD): ")
        atrasadas = tm.get_overdue(data)
        for t in atrasadas:
            print(t)

    elif op == "6":
        ordenadas = tm.sort_tasks()
        for t in ordenadas:
            print(t)

    elif op == "7":
        relatorio = tm.generate_report()
        print("\n--- RELATÓRIO ---")
        for chave, valor in relatorio.items():
            print(f"{chave}: {valor}")

    elif op == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
