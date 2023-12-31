import os


RESET = "\033[00m"


def clear():
    return os.system("cls" if os.name == "nt" else "clear")


class fg:
    black = "\u001b[30m"
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    magenta = "\u001b[35m"
    cyan = "\u001b[36m"
    white = "\u001b[37m"

    def rgb(r, g, b):
        return f"\u001b[38;2;{r};{g};{b}m"


class bg:
    black = "\u001b[40m"
    red = "\u001b[41m"
    green = "\u001b[42m"
    yellow = "\u001b[43m"
    blue = "\u001b[44m"
    magenta = "\u001b[45m"
    cyan = "\u001b[46m"
    white = "\u001b[47m"

    def rgb(r, g, b):
        return f"\u001b[48;2;{r};{g};{b}m"


class style:
    reset = "\u001b[0m"
    bold = "\u001b[1m"
    underline = "\u001b[4m"
    reverse = "\u001b[7m"
