import socket

from http_parser import HttpParseError, parse_request


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 8000))

server.listen()

print("Nexum is listening on 127.0.0.1:8000")

connection, address = server.accept()

print(f"Client connected: {address}")

data = connection.recv(4096)

try:
    request = parse_request(data)

except HttpParseError as error:
    print(f"HTTP parsing failed: {error}")

    response = (
        "HTTP/1.1 400 Bad Request\r\n"
        "Content-Type: text/plain\r\n"
        "Content-Length: 11\r\n"
        "\r\n"
        "Bad Request"
    )

    connection.sendall(response.encode())

    connection.close()
    server.close()
    exit()

print("METHOD:", request.method)
print("PATH:", request.path)
print("VERSION:", request.version)
print("HEADERS:", request.headers)

response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/plain\r\n"
    "Content-Length: 5\r\n"
    "\r\n"
    "Hello"
)

connection.sendall(response.encode())

connection.close()
server.close()