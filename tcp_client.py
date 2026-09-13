import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 8000))

client.sendall(b"Hello Nexum")

data = client.recv(1024)

print(f"Server replied: {data!r}")

client.close()