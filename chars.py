from dataclasses import dataclass, field


@dataclass
class Char:
    name: str
    description: str = field(init=False)
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
