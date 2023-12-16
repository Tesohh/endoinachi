from chars import char_chunks, chars
from renderer import render_character, render_from_str

rendered_chunks: list[list[str]] = []
idx = 0
char_id = 1
for chunk in char_chunks:
    rendered_chunks.append([])
    for i in chunk:
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

for i in render_lines:
    for j in i:
        for k in j:
            print(k)
        print("END CHAR")
    print("END CHUNK")

for chunk in render_lines:
    for i in range(10):
        print(f"{chunk[0][i]}  {chunk[1][i]}  {chunk[2][i]}")
    print("")
