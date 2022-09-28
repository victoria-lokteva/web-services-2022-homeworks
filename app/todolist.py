from fastapi import FastAPI
from tasks import Task


class ToDoListApi(FastAPI):
    pass


class ToDoList():

    def __init__(self):
        self.task_list = []

    def add_task(self, user, name, description, deadline):
        task = Task(user=user, name=name, description=description, deadline=deadline, is_complited=False)
        self.task_list.append(task)

    def send_notification(self, today, task):
        pass

    def mark_as_completed(self, task):
        task.is_complited = True

    def number_of_tasks(self):
        return len(self.task_list)
