from parameterized import parameterized
import unittest
from datetime import date
from ..todolist import ToDoList
from ..tasks import Task


class IntegrationTests(unittest.TestCase):

    def test_adding_task(self):
        @parameterized.expand([
            ["Call grandma", None, date(year=2022, month=11, day=11), 1],
            ["Hairdresser appointment", "Calle Lima at 11 a.m. ", date(year=2022, month=10, day=29), 2]
        ])
        def test_sequence(task_name, task_description, deadline, number_of_tasks):
            todo = ToDoList()
            task = Task()
            task.task_name = task_name
            task.task_description = task_description
            task.deadline = deadline
            todo.add_task(task)
            self.assertEqual(todo.number_of_tasks(), number_of_tasks)

    def test_notification_system(self):
        @parameterized.expand([
            ["Buy a washing machine", None, date(year=2020, month=4, day=12), False],
            ["Dental appointment", "Visit Medical Center at 9 a.m. ", date(year=2022, month=9, day=29), True],
            ["Symphony", "Write my first symphony", date(year=2023, month=3, day=30), False],
        ])
        def test_sequence(task_name, task_description, deadline, send_notification):
            todo = ToDoList()
            task = Task()
            task.task_name = task_name
            task.task_description = task_description
            task.deadline = deadline
            today = date(year=2022, month=9, day=28)
            self.assertTrue(todo.send_notification(today, task), send_notification)
