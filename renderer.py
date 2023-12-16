import chars
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


def render_from_str(input: str, number=0) -> str:
    s = ""
    lines = input.split()
    for l in lines:
        for c in l:
            s += letter2color[c] + "█" + color.RESET
        s += "\n"

    b = [char for char in s]
    if number != 0:
        b.insert(0, f"{color.fg.black}{color.bg.white}{number}")
        b.pop(6)
        b.pop(5)
    temp = ""
    for i in b:
        temp += i

    return temp[:-1]  # [:-1] is used to remove the last \n


def render_character(char: chars.Char, number=0) -> str:
    f = open(char.image_path)
    rf = f.read()
    f.close()

    return render_from_str(rf, number)


def render_chunks(pulled_down: list[int] = []) -> str:
    rendered_chunks: list[list[str]] = []
    idx = 0
    char_id = 1
    for chunk in chars.char_chunks:
        rendered_chunks.append([])
        for i in chunk:
            if char_id - 1 in pulled_down:
                rendered_chunks[idx].append(render_character(chars.x))
            else:
                rendered_chunks[idx].append(render_character(i, char_id))
            char_id += 1
        idx += 1

    render_lines: list[list[list[str]]] = []
    idx_x = 0
    for chunk in rendered_chunks:
        render_lines.append([])
        for char in chunk:
            render_lines[idx_x].append(char.splitlines())
        idx_x += 1

    s = ""
    for chunk in render_lines:
        for i in range(10):
            s += f"{chunk[0][i]}  {chunk[1][i]}  {chunk[2][i]}\n"
        s += "\n"

    return s
