import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 8000))

server.listen()

print("Nexum is listening on 127.0.0.1:8000")

connection, address = server.accept()

print(f"Client connected: {address}")

data = connection.recv(1024)

print(f"Received: {data!r}")

connection.sendall(b"Hello from Nexum")

connection.close()
server.close()