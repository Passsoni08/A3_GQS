#Arquivo para refatoração do código

from datetime import datetime
import uuid

class Task:
    
      #  Classe para representar uma tarefa individual
      #  Método para verificar se a tarefa está atrasada
    
    
    def __init__(self, name, priority, due_date, completed=False):
        self.id = str(uuid.uuid4())  # ID único para cada tarefa
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def is_overdue(self, current_date):
        
          #  Verifica se a tarefa está atrasada
        
        current = datetime.strptime(current_date, "%Y-%m-%d")
        due = datetime.strptime(self.due_date, "%Y-%m-%d")
        return not self.completed and due < current

    def __repr__(self):
        # Gera uma representação da tarefa
        
        return (f"{self.id[:8]} | {self.name} | Prioridade: {self.priority} | "
                f"Entrega: {self.due_date} | Feita: {self.completed}")


class TaskManager:
    
    # Gerenciar coleção de tarefas
    # Funcionalidades
    # Filtrar
    
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority, due_date):
        
        # Valida dados fornecidos
        # Lança erros
        
        if priority not in ["baixa", "média", "alta"]:
            raise ValueError("Prioridade inválida. Use: baixa, média ou alta.")
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Data inválida. Use o formato YYYY-MM-DD.")
        task = Task(name, priority, due_date)
        self.tasks.append(task)

    def complete_task(self, task_id):
        
        # Procurar e completar tarefa
        
        for task in self.tasks:
            if task.id.startswith(task_id):  # Permite busca parcial
                task.completed = True
                return True
        return False

    def list_tasks(self):
        return [repr(task) for task in self.tasks]

    def filter_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def get_overdue(self, current_date):
        return [task for task in self.tasks if task.is_overdue(current_date)]

    def sort_tasks(self):
        return sorted(self.tasks, key=lambda t: (t.completed, t.due_date))

    def generate_report(self):
        
        # Gerar relatório
        
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
