from dataclasses import dataclass
import socket


@dataclass
class ClientConn:
    sock: socket.socket
    addr: (str, int)

    def start(self):
        while True:
            req = self.sock.recv(1024)
            self.sock
            if not req:  # in case the connection is closed:
                # server.unregister??
                print(self.sock.getsockname(), "disconnected!")
                self.sock.close()
                return

            req = req.decode("utf-8")
            print(req, end="")
