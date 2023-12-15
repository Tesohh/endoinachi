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
            do_i_quit = self.handle_msg(msg)
            if do_i_quit:
                return

    def handle_msg(self, msg: Msg) -> bool:
        match msg.action:
            case "selected_char":
                self.selected_char_id = msg.data["char_id"]
                print("CISSY", self.selected_char_id)
                self.serv.ready_players += 1
            case "turn_done":
                self.serv.current_player = (
                    self.serv.p1
                    if self.serv.current_player == self.serv.p2
                    else self.serv.p2
                )
                self.serv.current_player.send(Msg("your_turn", {}))
            case "guess":
                guessed = int(msg.data["char_id"])

                self.other_conn.send(Msg("other_guess", {"char_id": guessed}))

                print(guessed, self.selected_char_id, self.other_conn.selected_char_id)
                if guessed == self.other_conn.selected_char_id:
                    self.send(
                        Msg("win", {"reason": "hai indovinato il personaggio giusto"})
                    )
                    self.other_conn.send(
                        Msg("lose", {"reason": "L'altro giocatore ha indovinato!"})
                    )
                else:
                    self.send(Msg("lose", {"reason": "Hai smarciato tutto"}))
                    self.other_conn.send(
                        Msg("win", {"reason": "L'altro giocatore NON ha indovinato!"})
                    )

    def send(self, msg: Msg):
        self.sock.send(bytes(msg.toJson(), "utf-8"))
