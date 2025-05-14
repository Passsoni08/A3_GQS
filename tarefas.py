#Arquivo para refatoração do código

from datetime import datetime

class Task:
    """
    Representa uma tarefa individual.
    Responsável apenas por armazenar dados e verificar vencimento.
    Aplica o princípio SRP (Single Responsibility Principle).
    """

    def __init__(self, name, priority, due_date, completed=False):
        self.name = name
        self.priority = priority
        self.due_date = due_date  # Espera uma string no formato YYYY-MM-DD
        self.completed = completed

    def is_overdue(self, current_date):
        """
        Verifica se a tarefa está atrasada comparando com a data atual.
        current_date deve ser uma string no formato YYYY-MM-DD.
        """
        return not self.completed and self.due_date < current_date

    def __repr__(self):
        """
        Representação legível da tarefa, útil para listagem.
        """
        return f"{self.name} | Prioridade: {self.priority} | Entrega: {self.due_date} | Feita: {self.completed}"


class TaskManager:
    """
    Classe responsável por gerenciar uma lista de tarefas.
    Contém funcionalidades como adicionar, listar, ordenar, filtrar, etc.
    Aplica os princípios SRP, OCP e DRY.
    """

    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority, due_date):
        """
        Adiciona uma nova tarefa à lista.
        """
        task = Task(name, priority, due_date)
        self.tasks.append(task)

    def complete_task(self, name):
        """
        Marca uma tarefa como concluída, buscando pelo nome.
        """
        for task in self.tasks:
            if task.name == name:
                task.completed = True
                break

    def list_tasks(self):
        """
        Retorna uma lista de strings representando cada tarefa.
        """
        return [repr(task) for task in self.tasks]

    def filter_by_priority(self, priority):
        """
        Retorna uma lista de tarefas com a prioridade especificada.
        """
        return [task for task in self.tasks if task.priority == priority]

    def get_overdue(self, current_date):
        """
        Retorna as tarefas que estão atrasadas em relação à data fornecida.
        """
        return [task for task in self.tasks if task.is_overdue(current_date)]

    def sort_tasks(self):
        """
        Ordena as tarefas por status (incompletas primeiro) e depois pela data.
        """
        return sorted(self.tasks, key=lambda t: (t.completed, t.due_date))

    def generate_report(self):
        """
        Gera um dicionário com contagem de prioridades, concluídas e total.
        Aplica o princípio DRY usando dicionários em vez de variáveis repetidas.
        """
        priorities = {"alta": 0, "média": 0, "baixa": 0}
        completed = sum(task.completed for task in self.tasks)

        for task in self.tasks:
            if task.priority in priorities:
                priorities[task.priority] += 1

        return {
            "Alta prioridade": priorities["alta"],
            "Média prioridade": priorities["média"],
            "Baixa prioridade": priorities["baixa"],
            "Concluídas": completed,
            "Total": len(self.tasks),
        }
