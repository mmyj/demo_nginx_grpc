import sys

import grpc

sys.path.append('/protos/gen')
sys.path.append('/venv/lib/python3.8/site-packages')

import hello_pb2
import hello_pb2_grpc
import hello_again_pb2
import hello_again_pb2_grpc


def run():
    for i in range(1, 10):
        print('The No {} greeter'.format(i))

        with grpc.insecure_channel('nginx_1:8088') as channel:
            stub = hello_pb2_grpc.GreeterStub(channel)
            response = stub.SayHello(hello_pb2.HelloRequest(name='alice-{}'.format(i)))
            print("Greeter client received: " + response.message)

        with grpc.insecure_channel('nginx_1:8088') as channel:
            stub = hello_again_pb2_grpc.GreeterAgainStub(channel)
            response = stub.SayHelloAgain(hello_again_pb2.HelloAgainRequest(name='alice-{}'.format(i)))
            print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
