
## Homework-1

Hello world in FastAPI

## Homework-2

Web-application stores user's to-do list and deadline for every task.
Application sends notifications, that deadline for a task is upcoming.
When a user completes a task, he can mark this task as completed.

A user can:

*to register

*to create a task

*to mark a task as completed


Command to launch tests:

Integration tests:

 python3.10 -m unittest discover -s app/  -p "*integration_test.py"

Unit tests:

pytest tests/unit_test.py


## Homework 3

gRPC to-do-list application

Command to compile proto file:  python3 -m grpc_tools.protoc -I grpc_app/ --python_out=grpc_app/builds/ --grpc_python_out=grpc_app/builds/ grpc_app/server.proto


To run service: python3.10 ./grpc/service.py

To run client: python3.10 ./grpc/client.py

To run tests: python3.10 -m unittest discover -s app/ -p "*tests.py"