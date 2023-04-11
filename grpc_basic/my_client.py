from concurrent import futures
import time
import grpc
from grpc_python_out import hello_world_pb2_grpc
from grpc_python_out import hello_world_pb2


# First, we define a function that will be called when the python file is called from the terminal
# This will first begin by creating an insecure connection to the localhost server at the same port as the
# grpc server.
# Then, we need to initialize the Stub for the grpc service, and pass the channel into it.
def client():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_world_pb2_grpc.GreetingServiceStub(channel)
        # we can take an input from the user here, or we can directly call this function
        # based on some logic.
        rpc_call = input('What is your name ? \n ')  # Always try to name the client input variable as 'rpc_call'
        # import ipdb
        # ipdb.set_trace()

        if rpc_call:
            print('Request received\n\n' + rpc_call)
            hello_request = hello_world_pb2.HelloRequest(name=rpc_call)
            hello_reply = stub.SayHello(hello_request)
            print(f'Response received::: {hello_reply}')


if __name__ == '__main__':
    client()
