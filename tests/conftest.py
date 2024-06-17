import pytest
import grpc

from utils.api.grpc import grpc_example_service_pb2_grpc


@pytest.fixture()
def grpc_stub():
    channel = grpc.insecure_channel('localhost:50051')
    stub = grpc_example_service_pb2_grpc.GrpcExampleServiceStub(channel)
    yield stub
    channel.close()
