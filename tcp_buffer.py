class TcpBuffer:

    def __init__(self):
        self.data = b""

    def append(self, chunk):
        self.data += chunk

    def has_complete_headers(self):
        return b"\r\n\r\n" in self.data

    def extract_headers(self):
        marker = b"\r\n\r\n"

        if marker not in self.data:
            return None

        end = self.data.index(marker) + len(marker)

        headers = self.data[:end]

        self.data = self.data[end:]

        return headers

    def get_data(self):
        return self.data