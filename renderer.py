from chars import Char
import color

letter2color = {
    "0": color.RESET,
    "n": color.fg.black,
    "r": color.fg.rgb(210, 179, 172),
    "b": color.fg.red,
    "w": color.fg.white,
    "m": color.fg.rgb(88, 57, 39),
    "a": color.fg.blue,
    "f": color.fg.red,
    "g": color.fg.rgb(40, 40, 40),
    "p": color.fg.yellow,
}


def render_from_str(input: str) -> str:
    s = ""
    lines = input.split()
    for l in lines:
        for c in l:
            s += letter2color[c] + "█" + color.RESET
        s += "\n"
    return s[:-1]  # [:-1] is used to remove the last \n


def render_character(char: Char) -> str:
    f = open(char.image_path)
    zesty = f.read()

    return render_from_str(zesty)
