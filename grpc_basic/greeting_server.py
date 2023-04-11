from concurrent import futures
import time
import grpc
from grpc_python_out import greeting_pb2_grpc
from grpc_python_out import greeting_pb2
# First we define a class that will be responsible for handling the data through methods.
# This class will serialize and deserialize the data.
# It will inherit from the Servicer class in the pb2_grpc.py file. With rpc methods as described in the protofile


class Greetings(greeting_pb2_grpc.GreetingsServicer):
    def SayHello(self, request, context):   # This method exists in the parent class.
        # We can override it for our purposes
        print(f'Request received :::: {request}')
        time.sleep(5)
        hello_reply = greeting_pb2.HelloReply()
        hello_reply.message = f'{request.name}' # This will give message key in the response
        # and we can use the above methodology to get differnet attributes with custom logic of
        # fetching the data.
        # In this case we have used 'message' attribute since we have specified it in the protofile
        # as you can notice, request has an attribute 'name'
        # This is present in the protofile as well.
        print(f'Sending response ::: {hello_reply}')
        return hello_reply

    def DrawHello(self, image, name):
        return super().DrawHello(image, name)

    def ImageHello(self, request_iterator, context):
        return super().ImageHello(request_iterator, context)

    def VideoHello(self, request_iterator, context):
        return super().VideoHello(request_iterator, context)


# Next we need to create a serve method that will be called and will act like a server
def serve():
    # For this, we need to create a grpc.server instance, lets call it 'server'.
    # We need to provide thread_pool argument since it is a required argument
    print("Server started at 'localhost:50051'")
    server = grpc.server(thread_pool=futures.ThreadPoolExecutor(max_workers=4))
    print(" Thread pool executor initialized with max limit of 4 workers")
    # Next we need to call the 'add_<SERVICERCLASSNAME>_to_server method from the parent class
    # and pass the Class and the server instance in this method
    greetings_service = Greetings()
    greeting_pb2_grpc.add_GreetingsServicer_to_server(greetings_service, server)
    # Next we need to add a port for the server to listen on
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()


