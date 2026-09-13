class HttpParseError(Exception):
    pass


class HttpRequest:

    def __init__(self, method, path, version, headers):
        self.method = method
        self.path = path
        self.version = version
        self.headers = headers


def parse_request(data):

    try:
        text = data.decode("utf-8")

    except UnicodeDecodeError as error:
        raise HttpParseError(
            "Request contains invalid UTF-8"
        ) from error

    header_section = text.split("\r\n\r\n", 1)[0]

    lines = header_section.split("\r\n")

    if not lines or not lines[0]:
        raise HttpParseError("Missing request line")

    request_line = lines[0]

    parts = request_line.split(" ")

    if len(parts) != 3:
        raise HttpParseError("Invalid request line")

    method, path, version = parts

    if not method or not path or not version:
        raise HttpParseError("Invalid request line")

    headers = {}

    for line in lines[1:]:

        if not line:
            continue

        if ":" not in line:
            raise HttpParseError("Invalid header")

        name, value = line.split(":", 1)

        name = name.strip()
        value = value.strip()

        if not name:
            raise HttpParseError("Invalid header")

        headers[name] = value

    return HttpRequest(
        method=method,
        path=path,
        version=version,
        headers=headers,
    )