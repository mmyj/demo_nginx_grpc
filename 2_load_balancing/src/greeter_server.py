import os
import sys
from concurrent import futures

import grpc

sys.path.append('/protos/gen')
sys.path.append('/venv/lib/python3.8/site-packages')

import hello_pb2
import hello_pb2_grpc


class Greeter(hello_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message='Hello, {}!, I am {}'.format(request.name, os.getenv("HOST_NAME")))


def serve():
    print("grpc server {} starting".format(os.getenv("HOST_NAME")))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    print("grpc server {} started".format(os.getenv("HOST_NAME")))
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
