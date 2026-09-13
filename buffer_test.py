from tcp_buffer import TcpBuffer


buffer = TcpBuffer()

buffer.append(
    b"GET /hello HTTP/1.1\r\n"
    b"Host: localhost\r\n"
    b"\r\n"
    b"GET /second HTTP/1.1\r\n"
    b"Host: localhost\r\n"
    b"\r\n"
)

first_request = buffer.extract_headers()

print("First request:")
print(first_request)

print()

print("Remaining buffer:")
print(buffer.get_data())