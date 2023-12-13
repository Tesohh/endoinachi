from dataclasses import dataclass, field
import socket
from chars import Char, chars

from msg import Msg, fromJson
from serverconn import ServerConn


@dataclass
class Client:
    server_conn: ServerConn
    selected_char: int = field(init=False)

    def start(self):
        while True:
            req = self.server_conn.sock.recv(1024)
            if not req:
                raise Exception("failed getting messages from server")
            msg = fromJson(req)
            self.handle_msg(msg)

    def handle_msg(self, msg: Msg):
        match msg.action:
            case "ready":
                for i in range(len(chars)):
                    print(i + 1, chars[i].name)

                while True:
                    self.selected_char = int(input("scegli > ")) - 1
                    if self.selected_char >= 0 and self.selected_char < len(chars):
                        break

                self.server_conn.send(
                    Msg("selected_char", {"char_id": self.selected_char})
                )


HOST = "localhost"
PORT = 42069

client: Client

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    client = Client(ServerConn(sock))
    client.start()
