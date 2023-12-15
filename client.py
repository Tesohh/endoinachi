from dataclasses import dataclass, field
import socket
from chars import Char, chars
import color
from msg import Msg, fromJson
from serverconn import ServerConn


def print_chars(skip: list[int] = []):
    for i in range(len(chars)):
        if i not in skip:
            print(i + 1, chars[i].name)
        else:
            print(f"{color.fg.black}{i + 1} {chars[i].name}{color.RESET}")


@dataclass
class Client:
    server_conn: ServerConn
    selected_char: int = field(init=False)
    pulled_down: list[int] = field(init=False, default_factory=lambda: [])

    def start(self):
        while True:
            req = self.server_conn.sock.recv(1024)
            if not req:
                raise Exception("failed getting messages from server")
            msg = fromJson(req)
            do_i_quit = self.handle_msg(msg)
            if do_i_quit:
                return

    def handle_msg(self, msg: Msg) -> bool:
        match msg.action:
            case "ready":
                color.clear()
                print_chars()

                while True:
                    self.selected_char = int(input("scegli > ")) - 1
                    if self.selected_char >= 0 and self.selected_char < len(chars):
                        break

                color.clear()
                self.server_conn.send(
                    Msg("selected_char", {"char_id": self.selected_char})
                )
                print("aspetto l'altro...")

            case "game_started":
                color.clear()
                print("cissy si gioca")

            case "your_turn":
                color.clear()
                print_chars(self.pulled_down)

                selected = 999

                def all_selected():
                    return len(self.pulled_down) >= len(chars)

                while selected != -1 and not all_selected():
                    selected = int(input("scegli (0 per passare il turno) > ")) - 1
                    if selected == -1:
                        print("BASTA")
                        break
                    if (
                        selected >= 0
                        and selected < len(chars)
                        and selected not in self.pulled_down
                    ):
                        self.pulled_down.append(selected)
                        color.clear()
                        print_chars(self.pulled_down)
                        self.server_conn.send(Msg("pull_down", {"char_id": selected}))

                if all_selected():
                    print("ipotesi: " + chars[self.pulled_down[-1]].name)
                    self.server_conn.send(
                        Msg("guess", {"char_id": self.pulled_down[-1]})
                    )
                else:
                    print("do il turno all'altro...")
                    color.clear()
                    print_chars(self.pulled_down)
                    self.server_conn.send(Msg("turn_done", {}))
                    print("aspetto l'altro...")
            case "other_guess":
                guessed = int(msg.data["char_id"])
                print(f"L'altro ha un ipotesi: {chars[guessed].name}")
            case "win":
                print(f"Hai vinto! {msg.data['reason']}")
                return True
            case "lose":
                print(f"Hai perso! {msg.data['reason']}")
                return True


HOST = "localhost"
PORT = 42069

client: Client

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    client = Client(ServerConn(sock))
    client.start()
