from dataclasses import dataclass, field


@dataclass
class Char:
    name: str
    description: str
    image: str = field(init=False)


chars = [
    Char("Harry", "incredibilmente incredibilus"),
    Char("playtoy party", "00pium"),
    Char("cheff kif", "oblockkk"),
    Char("yesking", "how good is that cylinder"),
    Char("ay brodie", "hol on hol don"),
    Char("ROLI", "IL DON"),
    Char("cro", "la minaccia di cavalese"),
    Char("snusman", "O GIRATI..."),
    Char("ZIZZOMINZY", "forse e' cro? non lo sapremo mai"),
]
