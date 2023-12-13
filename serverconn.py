from dataclasses import dataclass
import socket

from msg import Msg


@dataclass
class ServerConn:
    sock: socket.socket

    def send(self, msg: Msg):
        self.sock.send(bytes(msg.toJson(), "utf-8"))
