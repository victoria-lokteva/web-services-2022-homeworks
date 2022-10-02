import grpc
from concurrent.futures import ThreadPoolExecutor
import datetime
from grpc_app.builds.server_pb2_grpc import ProcessTasksServicer, add_ProcessTasksServicer_to_server
from grpc_app.builds.server_pb2 import Response_completed, Response_added


class Service(ProcessTasksServicer):
    def AddTask(self, request):
        days = request.dealine - datetime.utcnow()
        return Response_added(days_before_deadline=days, added=True)

    def CompleteTask(self):
        return Response_completed(completed=True)


def execute_service():
    server = grpc.server(ThreadPoolExecutor(num_workers=10))
    server.add_ProcessTasksServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:3000")
    server.start()
    server.wait_for_termination()
