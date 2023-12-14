from dataclasses import dataclass, field
import json
import socket
from typing import Any, Self
from msg import Msg, fromDict, fromJson


@dataclass
class ClientConn:
    sock: socket.socket
    other_conn: Self = field(init=False)  # keeps a reference of the other connection
    serv: Any = field(init=False)
    addr: (str, int)

    selected_char_id: int = field(init=False)

    def start(self):
        while True:
            req = self.sock.recv(1024)
            if not req:  # in case the connection is closed:
                # server.unregister??
                print(self.sock.getsockname(), "disconnected!")
                self.sock.close()
                return

            req = req.decode("utf-8")
            msg = fromJson(req)
            self.handle_msg(msg)

    def handle_msg(self, msg: Msg):
        match msg.action:
            case "selected_char":
                self.selected_char_id = msg.data["char_id"]
                self.serv.ready_players += 1

    def send(self, msg: Msg):
        self.sock.send(bytes(msg.toJson(), "utf-8"))
