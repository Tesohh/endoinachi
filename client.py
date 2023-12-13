from dataclasses import dataclass, field
import socket

from msg import Msg, fromJson


@dataclass
class Client:
    # server_conn: ServerConn
    sock: socket.socket
    selected_char: str = field(init=False)

    def start(self):
        while True:
            req = self.sock.recv(1024)
            if not req:
                raise Exception("failed getting messages from server")
            msg = fromJson(req)
            self.handle_msg(msg)

    def handle_msg(self, msg: Msg):
        match msg.action:
            case "ready":
                print("ready")


HOST = "localhost"
PORT = 42069

client: Client

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    client = Client(sock)
    client.start()
