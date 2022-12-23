import socket


class Server:
    def __init__(self, port=55000):
        self.addr = None
        self.conn = None
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', port))
        self.sock.listen(2)

    def start(self):
        print('Server is running.')
        while True:
            self.conn, self.addr = self.sock.accept()
            print('connected:', self.addr)
            data = self.conn.recv(1024)
            print(str(data))
            self.conn.send(data.upper())

    def stop(self):
        if self.conn is None:
            return

        self.conn.close()


if __name__ == "__main__":
    server = Server(55000)
    server.start()
    server.stop()
