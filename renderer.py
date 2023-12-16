from chars import Char
import color

letter2color = {
    "0": color.RESET,
    "n": color.fg.black,
    "r": color.fg.magenta,
    "b": color.fg.red,
    "w": color.fg.white,
    "m": color.fg.rgb(255, 248, 220),
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
