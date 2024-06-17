from utils.api.grpc import grpc_example_service_pb2


def test_add_client_one_amounts_successfully(grpc_stub):
    client_info = grpc_example_service_pb2.ClientInfoRequest(login="user5", email="user4@example.com", city="City4")
    request = grpc_example_service_pb2.ClientsInfoRequest(clientsinfo=[client_info])
    response = grpc_stub.AddClient(request)
    assert response.WhichOneof('Response') == 'response_ok', f"Error: {response.response_error.message}"


def test_add_client_two_amounts_successfully(grpc_stub):
    client_info_one = grpc_example_service_pb2.ClientInfoRequest(login="user6", email="user4@example.com", city="City4")
    client_info_two = grpc_example_service_pb2.ClientInfoRequest(login="user7", email="user4@example.com", city="City4")
    request = grpc_example_service_pb2.ClientsInfoRequest(clientsinfo=[client_info_one, client_info_two])
    response = grpc_stub.AddClient(request)
    assert response.WhichOneof('Response') == 'response_ok', f"Error: {response.response_error.message}"
