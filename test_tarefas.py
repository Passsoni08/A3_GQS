#Arquivo para testes automatizados

import unittest
from tarefas import TaskManager
from datetime import datetime

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tm = TaskManager()
        self.tm.add_task("Estudar", "alta", "2025-05-01")
        self.tm.add_task("Lavar roupa", "média", "2025-04-25")
        self.tm.add_task("Comprar pão", "baixa", "2025-04-28")

    def test_add_task(self):
        self.tm.add_task("Nova tarefa", "alta", "2025-06-01")
        self.assertEqual(len(self.tm.tasks), 4)
        self.assertEqual(self.tm.tasks[-1].name, "Nova tarefa")

    def test_complete_task(self):
        tarefa_id = self.tm.tasks[0].id[:8]
        result = self.tm.complete_task(tarefa_id)
        self.assertTrue(result)
        self.assertTrue(self.tm.tasks[0].completed)

    def test_complete_task_fail(self):
        result = self.tm.complete_task("inexistente")
        self.assertFalse(result)

    def test_filter_by_priority(self):
        media = self.tm.filter_by_priority("média")
        self.assertEqual(len(media), 1)
        self.assertEqual(media[0].name, "Lavar roupa")

    def test_get_overdue(self):
        overdue = self.tm.get_overdue("2025-04-29")
        nomes = [t.name for t in overdue]
        self.assertIn("Lavar roupa", nomes)
        self.assertIn("Comprar pão", nomes)
        self.assertNotIn("Estudar", nomes)

    def test_sort_tasks(self):
        self.tm.complete_task(self.tm.tasks[2].id[:8])
        ordenadas = self.tm.sort_tasks()
        self.assertFalse(ordenadas[0].completed)
        self.assertTrue(ordenadas[-1].completed)

    def test_generate_report(self):
        self.tm.complete_task(self.tm.tasks[0].id[:8])
        relatorio = self.tm.generate_report()
        self.assertEqual(relatorio["Alta prioridade"], 1)
        self.assertEqual(relatorio["Média prioridade"], 1)
        self.assertEqual(relatorio["Baixa prioridade"], 1)
        self.assertEqual(relatorio["Concluídas"], 1)
        self.assertEqual(relatorio["Total"], 3)

if __name__ == '__main__':
    unittest.main()
