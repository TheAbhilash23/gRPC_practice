from concurrent import futures
import time
import grpc
from grpc_python_out import greeting_pb2_grpc
from grpc_python_out import greeting_pb2


# First, we define a function that will be called when the python file is called from the terminal
# This will first begin by creating an insecure connection to the localhost server at the same port as the
# grpc server.
# Then, we need to initialize the Stub for the grpc service, and pass the channel into it.
def client(rpc_method):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeting_pb2_grpc.GreetingsStub(channel)
        match rpc_method:
            case 'SayHello':
                # we can take an input from the user here, or we can directly call this function
                # based on some logic.
                rpc_call = input(
                    'What is your name ? \n ')  # Always try to name the client input variable as 'rpc_call'
                # import ipdb
                # ipdb.set_trace()

                if rpc_call:
                    print('Request received\n\n' + rpc_call)
                    hello_request = greeting_pb2.HelloRequest(name=rpc_call)
                    hello_reply = stub.SayHello(hello_request)
                    print(f'Response received::: {hello_reply}')
            case 'DrawHello':
                pass
            case 'ImageHello':
                pass
            case 'VideoHello':
                pass


if __name__ == '__main__':
    method = input('Enter RPC method from \n'
                   'SayHello\n'
                   'DrawHello\n'
                   'ImageHello\n'
                   'VideoHello\n'
                   )
    client(method)
