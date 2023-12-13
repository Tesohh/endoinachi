from dataclasses import dataclass
import json
import typing


@dataclass
class Msg:
    action: str
    data: dict

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


def fromDict(msg_dict: dict) -> Msg:
    msg = Msg("", {})
    for k, _ in typing.get_type_hints(msg).items():
        if msg_dict.get(k) is not None:
            setattr(msg, k, msg_dict[k])

    return msg


def fromJson(jstr: str) -> Msg:
    try:
        data = json.loads(jstr)
        return fromDict(data)
    except json.JSONDecodeError:
        print("couldn't decode message")
