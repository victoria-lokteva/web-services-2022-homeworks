import grpc
from grpc_app.builds.server_pb2_grpc import ProcessTasksStub
from grpc_app.builds.server_pb2 import Task


def main():
    with grpc.insecure_channel("localhost:3000") as channel:
        client = ProcessTasksStub(channel)
        response = client.AddTask(Task(name='test',
                                       description='to do test',
                                       deadline='28.08.2023',
                                       is_complited=False
                                       ))
        print(response.added, response.days_before_deadline)


if __name__ == "__main__":
    main()
