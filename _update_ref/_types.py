from typing import TypedDict


class Input(TypedDict):
    description: str
    required: bool
    default: str


class Action(TypedDict):
    name: str
    description: str
    inputs: dict[str, Input]
