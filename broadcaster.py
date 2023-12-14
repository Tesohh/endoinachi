from dataclasses import dataclass
from msg import Msg
import server


@dataclass
class Broadcaster:
    server: server.Server

    def broadcast(self, msg: Msg):
        self.server.p1.send(msg)
        self.server.p2.send(msg)

    def send_to_other(self, msg: Msg, sender):
        if sender == self.server.p1:
            self.server.p2.send(msg)
        elif sender == self.server.p2:
            self.server.p1.send(msg)


broadcaster = Broadcaster(server.server)
