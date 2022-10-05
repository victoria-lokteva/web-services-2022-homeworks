import unittest
import datetime
from parameterized import parameterized
import grpc
from concurrent.futures import ThreadPoolExecutor
from ..server import Service
from grpc_app.builds.server_pb2 import Task


class Test(unittest.TestCase):

    def __init__(self):
        self.port = 3000
        self.server = grpc.server(ThreadPoolExecutor(num_workers=10))
        self.server.add_ProcessTasksServicer_to_server(Service(), self.server)
        self.server.add_insecure_port(self.port)
        self.server.start()

    def test_adding_task(self):
        @parameterized.expand([
            ["Call grandma", None, '20.02.2023'],
            ["Plantar un arbol", "Plantar roble o arce", '14.04.2023']
        ])
        def test(task_name, task_description, deadline):
            response = self.server.add_task(Task(name=task_name, description=task_description, deadline=deadline))
            self.assertTrue(response.added)
            days = datetime.utcnow() - deadline
            self.assertEqual(response.days_before_deadline, days)

    def test_completing_task(self):
        @parameterized.expand([
            ["Call grandma", None, '20.02.2023'],
            ["Plantar un arbol", "Plantar roble o arce", '14.04.2023']
        ])
        def test(task_name, task_description, deadline):
            response = self.server.complete_task(Task(name=task_name, description=task_description,
                                                      deadline=deadline))
            self.assertTrue(response)
