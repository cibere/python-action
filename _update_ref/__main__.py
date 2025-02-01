from pathlib import Path
import yaml
import json
from typing import Iterator
from ._types import Action
from .input import Input

ci_dir = Path(__file__).parent
root = ci_dir.parent
action_file = root / "action.yml"
readme = root / "README.md"

HEADER = "## Input Reference"


def get_inputs() -> Iterator[Input]:
    raw = action_file.read_text()
    data: Action = yaml.safe_load(raw)

    print("--- Action Info ---")
    print(json.dumps(data, indent=4))

    for name, inp in data["inputs"].items():
        yield Input(
            name=name,
            description=inp["description"],
            required=inp["required"],
            default=inp.get("default", ""),
        )


def add_to_readme(text: str):
    total_content = readme.read_text()
    content = total_content.split(HEADER)[0]
    new_content = content + "\n" + text
    readme.write_text(new_content)


def main():
    parts = [HEADER]
    for inp in get_inputs():
        parts.append(inp.formatted())

    add_to_readme("\n".join(parts))


if __name__ == "__main__":
    main()
