import sys

import grpc

sys.path.append('/protos/gen')
sys.path.append('/venv/lib/python3.8/site-packages')

import hello_pb2
import hello_pb2_grpc


def run():
    with grpc.insecure_channel('greeter_server:50051') as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name='you'))
        print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
