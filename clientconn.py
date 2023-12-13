from dataclasses import dataclass
import json
import socket

from msg import Msg, fromDict, fromJson


@dataclass
class ClientConn:
    sock: socket.socket
    addr: (str, int)

    def start(self):
        while True:
            self.send(Msg("cissy", {"gozzo": "pozzo"}))
            req = self.sock.recv(1024)
            self.sock
            if not req:  # in case the connection is closed:
                # server.unregister??
                print(self.sock.getsockname(), "disconnected!")
                self.sock.close()
                return

            req = req.decode("utf-8")
            msg = fromJson(req)
            print(msg)

    def handleMsg(self, msg: Msg):
        print("zicsy")

    def send(self, msg: Msg):
        self.sock.send(bytes(msg.toJson(), "utf-8"))
