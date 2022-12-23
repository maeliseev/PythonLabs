import socket


class Client:
    def __init__(self, ip="localhost", port=55000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))

    def sendMessage(self):
        message = input("Что передать? ")
        self.sock.send(bytes(message, encoding='UTF-8'))
        print(f"u send on server -> {message}")

    def close(self):
        self.sock.close()


if __name__ == "__main__":
    client = Client()
    client.sendMessage()
    client.close()
