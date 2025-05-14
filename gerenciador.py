# Código para refatoração
# Este sistema gerencia uma lista de tarefas, com funcionalidades como 
# adicionar, listar, filtrar, ordenar e gerar relatórios.

tasks = []  # Uso de variável global. Deve ser encapsulada em uma classe.

def add_task():
    # Responsável por entrada de dados e lógica ao mesmo tempo. Viola SRP (Single Responsibility Principle).
    name = input("Nome da tarefa: ")
    prio = input("Prioridade (baixa, média, alta): ")
    due = input("Data de entrega (YYYY-MM-DD): ")
    task = {"name": name, "priority": prio, "due_date": due, "completed": False}
    tasks.append(task)

def complete_task(name):
    # Busca linear e alteração direta em estrutura de dicionário. Pouca coesão.
    for task in tasks:
        if task["name"] == name:
            task["completed"] = True

def list_tasks():
    for t in tasks:
        print(f"{t['name']} | Prioridade: {t['priority']} | Entrega: {t['due_date']} | Feita: {t['completed']}")

def filter_by_priority(priority):
    return [t for t in tasks if t["priority"] == priority]

def get_overdue(current_date):
    # Comparação de datas como strings pode causar erro
    overdue = []
    for t in tasks:
        if not t["completed"] and t["due_date"] < current_date:
            overdue.append(t)
    return overdue

def sort_tasks():
    return sorted(tasks, key=lambda x: (x["completed"], x["due_date"]))

def generate_report():
    # Código repetitivo para contagem de prioridades
    print("----- Relatório de Tarefas -----")
    high = 0
    medium = 0
    low = 0
    completed = 0
    for t in tasks:
        if t["priority"] == "alta":
            high += 1
        elif t["priority"] == "média":
            medium += 1
        elif t["priority"] == "baixa":
            low += 1
        if t["completed"]:
            completed += 1
    print("Alta prioridade:", high)
    print("Média prioridade:", medium)
    print("Baixa prioridade:", low)
    print("Concluídas:", completed)
    print("Total:", len(tasks))

# Chamada de função no escopo global, com entrada de dados obrigatória
add_task()
generate_report()
