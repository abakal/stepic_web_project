import asyncore, socket

class Server(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(('', port))
        self.listen(11)

    def handle_accept(self):

        socket, address = self.accept()
        print ('Connection by', address)
        EchoHandler(socket)

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        self.data = self.recv(1024)
        if not self.data:
            self.close()
        if self.data=="close":
            self.close
        else:
            self.send(self.data)

s = Server('0.0.0.0', 2222)
asyncore.loop()
