from django.db import models
from opentelemetry import trace
from time import sleep

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

tracer = trace.get_tracer(__name__)

# Create your models here.
@tracer.start_as_current_span("do_smth")
def do_smth():
    sleep(0.02)
    return "done smth"

@tracer.start_as_current_span("grpc")
def hello():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    return("Greeter client received: " + response.message)