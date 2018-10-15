import socket


class ClientError(Exception):
    """Общий класс исключений клиента"""
    pass


class Client:
    def __init__(self, address, port, timeout=None):
        try:
            self.socket = socket.create_connection((address, port), timeout)
        except socket.error:
            raise ClientError

    def _read(self):
        """Получаем ответ сервера на запрос"""

        data = b""
        while not data.endswith(b"\n\n"):
            try:
                data += self.socket.recv(1024)
            except socket.error:
                raise ClientError

        decoded_data = data.decode()

        status, answer = decoded_data.split("\n", 1)
        answer = answer.strip()

        # если получили ошибку - бросаем исключение ClientError
        if status == "error":
            raise ClientError

        return answer

    def put(self, metric, value, timestamp=None):
        if timestamp is None:
            timestamp = str(int(time.time()))

        string = "put {} {} {}\n".format(metric, str(value), timestamp)
        try:
            self.socket.sendall(string.encode())
        except socket.error:
            raise ClientError

        self._read()

    def get(self, metric):
        string = "get {}\n".format(metric)
        try:
            self.socket.sendall(string.encode())
        except socket.error:
            raise ClientError

        answer = self._read()

        data = {}
        if answer == "":
            return data

        for row in answer.split("\n"):
            key, value, timestamp = row.split()
            if key not in data:
                data[key] = []
            data[key].append((int(timestamp), float(value)))

        return data

    def close(self):
        self.socket.close()
