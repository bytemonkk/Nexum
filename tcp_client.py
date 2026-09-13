# import socket

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# client.connect(("127.0.0.1", 8000))

# client.sendall(b"Hello Nexum")

# data = client.recv(1024)

# print(f"Server replied: {data!r}")

# client.close()

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 8000))

request = (
    "GET / HTTP/1.1\r\n"
    "Host: localhost\r\n"
    "\r\n"
)

client.sendall(request.encode())

data = client.recv(4096)

print(data.decode())

client.close()