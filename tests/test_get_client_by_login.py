from utils.api.grpc import grpc_example_service_pb2


def test_get_client_by_login(grpc_stub):
    request = grpc_example_service_pb2.GetClientByLoginRequest(login="user1")
    response = grpc_stub.GetClientByLogin(request)
    assert response.WhichOneof('Response') == 'response_clients', f"Error: {response.response_error.message}"
    assert len(response.response_clients.clients) > 0
    client = response.response_clients.clients[0]
    assert client.login == "user1"
    assert client.email == "user1@example.com"
    assert client.city == "City1"
