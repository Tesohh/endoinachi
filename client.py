from dataclasses import dataclass
import socket

from msg import fromJson


@dataclass
class Client:
    # server_conn: ServerConn
    sock: socket.socket
    selected_char: str


HOST = "localhost"
PORT = 42069

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    while True:
        req = sock.recv(1024)
        if not req:
            raise Exception("failed getting messages from server")
        msg = fromJson(req)
        print(msg)
