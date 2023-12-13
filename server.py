import socket
import traceback
from dataclasses import dataclass
from threading import Thread

from clientconn import ClientConn
from msg import Msg

HOST = "localhost"
PORT = 42069


@dataclass
class Server:
    p1: ClientConn
    p2: ClientConn
    sock: socket.socket


server: Server

# execute this block ONLY if running py server.py
# this is to prevent this code to run if we do `import server`
if __name__ == "__main__":
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversock.bind(("localhost", 42069))

    print(f"server ascolta su {HOST}:{PORT}")

    try:
        clients: list[ClientConn] = []
        for i in range(2):
            print(f"attendo il giocatore {i+1}")
            serversock.listen(0)

            sock, client_addr = serversock.accept()
            clients.append(ClientConn(sock, client_addr))

            print(f"giocatore {i+1} connesso")
            Thread(target=clients[i].start).start()

        server = Server(clients[0], clients[1], serversock)

    except (Exception, KeyboardInterrupt) as e:
        print("bye bye")
        if not (type(e) == KeyboardInterrupt):
            traceback.print_exc()

    # now you're done with connecting clients
    server.p1.send(Msg("ready", {}))
    server.p2.send(Msg("ready", {}))

    # fai si che la porta 42069 venga liberata
    # if "server" in locals():
    #     print("ZEST")
    #     server.p1.sock.close()
    #     server.p2.sock.close()
    # serversock.close()
