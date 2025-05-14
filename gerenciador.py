# Código legado original
# Este sistema gerencia uma lista de tarefas: adicionar, listar, filtrar, ordenar e gerar relatórios.

tasks = []  # Variável global — deve ser encapsulada em uma classe


def add_task():
    """
    Função para adicionar uma nova tarefa.
    Mistura entrada de dados (input) com lógica de negócio.
    Pode ser refatorada para aceitar parâmetros externos.
    Deveria fazer parte de uma classe 'TaskManager'.
    """
    name = input("Nome da tarefa: ")
    prio = input("Prioridade (baixa, média, alta): ")
    due = input("Data de entrega (YYYY-MM-DD): ")
    task = {"name": name, "priority": prio, "due_date": due, "completed": False}
    tasks.append(task)


def complete_task(name):
    """
    Marca uma tarefa como concluída.
    Busca por nome diretamente — pode gerar erro em caso de duplicidade.
    Idealmente delegar essa função a uma instância de objeto.
    """
    for task in tasks:
        if task["name"] == name:
            task["completed"] = True


def list_tasks():
    """
    Lista todas as tarefas.
    Depende de print, o que limita a reutilização.
    Pode retornar uma lista de strings.
    """
    for t in tasks:
        print(f"{t['name']} | Prioridade: {t['priority']} | Entrega: {t['due_date']} | Feita: {t['completed']}")


def filter_by_priority(priority):
    """
    Filtra tarefas por prioridade.
    Simples e eficiente.
    """
    return [t for t in tasks if t["priority"] == priority]


def get_overdue(current_date):
    """
    Retorna tarefas atrasadas.
    Comparação entre strings — pode gerar resultados incorretos.
    Idealmente utilizar objetos de data (datetime).
    """
    overdue = []
    for t in tasks:
        if not t["completed"] and t["due_date"] < current_date:
            overdue.append(t)
    return overdue


def sort_tasks():
    """
    Ordena as tarefas por status de conclusão e data.
    Ordenação funcional, mas depende de estrutura de dicionário.
    """
    return sorted(tasks, key=lambda x: (x["completed"], x["due_date"]))


def generate_report():
    """
    Gera um relatório de tarefas.
    Código repetitivo para contagem de prioridades.
    Pode ser simplificado com uso de dicionários.
    """
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


# A chamada abaixo impede testes automáticos
# Deve ser removida para separar interface de lógica de negócio
# add_task()
# generate_report()
