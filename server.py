import socket

def create_server():
    # TODO: Create a server socket using AF_INET and SOCK_STREAM
    # TODO: Bind it to localhost:8080
    # TODO: Set the socket to listen for connections
    pass

def parse_request(request):
    # TODO: Split the request into lines
    # TODO: Parse the first line to get method, path, and HTTP version
    # Return a dictionary with the parsed information
    pass

# Base template for the server
server_socket = create_server()
print("Server listening on localhost:8080...")

while True:
    client_socket, addr = server_socket.accept()
    # TODO: Receive data from client
    # TODO: Parse the request (call your function)
    # TODO: Send a basic response (e.g., "Hello World!")
    client_socket.close()
