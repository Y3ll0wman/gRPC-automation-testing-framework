from utils.api.grpc import grpc_example_service_pb2


def test_get_clients_success(grpc_stub):
    request = grpc_example_service_pb2.EmptyRequest()
    response = grpc_stub.GetClients(request)
    assert response.WhichOneof('Response') == 'response_clients', f"Error: {response.response_error.message}"
    assert len(response.response_clients.clients) > 0
