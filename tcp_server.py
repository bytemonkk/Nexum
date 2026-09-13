# import socket

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server.bind(("127.0.0.1", 8000))

# server.listen()

# print("Nexum is listening on 127.0.0.1:8000")

# connection, address = server.accept()

# print(f"Client connected: {address}")

# data = connection.recv(1024)

# print(f"Received: {data!r}")

# connection.sendall(b"Hello from Nexum")

# connection.close()
# server.close()

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 8000))

server.listen()

print("Nexum is listening on 127.0.0.1:8000")

connection, address = server.accept()

print(f"Client connected: {address}")

data = connection.recv(4096)

print(f"Received:\n{data.decode()}")

# connection.sendall(b"Hello from Nexum")

response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/plain\r\n"
    "Content-Length: 16\r\n"
    "\r\n"
    "Hello from Nexus"
)

connection.sendall(response.encode())

connection.close()
server.close()