import os
import sys
from concurrent import futures

import grpc

sys.path.append('/protos/gen')
sys.path.append('/venv/lib/python3.8/site-packages')

import hello_again_pb2
import hello_again_pb2_grpc


class GreeterAgain(hello_again_pb2_grpc.GreeterAgainServicer):
    def SayHelloAgain(self, request, context):
        return hello_again_pb2.HelloAgainReply(
            message='Hello again, {}!, I am {}'.format(request.name, os.getenv("HOST_NAME")))


def serve():
    print("grpc server {} starting".format(os.getenv("HOST_NAME")))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_again_pb2_grpc.add_GreeterAgainServicer_to_server(GreeterAgain(), server)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    print("grpc server {} started".format(os.getenv("HOST_NAME")))
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
