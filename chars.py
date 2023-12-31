from dataclasses import dataclass, field


@dataclass
class Char:
    name: str
    image_path: str = field(default="")


chars = [
    Char("Hera", "characters/hera"),
    Char("Cesco", "characters/cesco"),
    Char("Pallaver", "characters/matthias"),
    Char("Tesohh", "characters/tesohh"),
    Char("Alder", "characters/alder"),
    Char("Corny", "characters/corny"),
    Char("Zizzo", "characters/zizzominzy"),
    Char("Buccia", "characters/buccia"),
    Char("Rikilento", "characters/rikilento"),
]

char_chunks = [
    [chars[0], chars[1], chars[2]],
    [chars[3], chars[4], chars[5]],
    [chars[6], chars[7], chars[8]],
]

x = Char("x", "characters/x")
