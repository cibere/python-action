from pathlib import Path
import textwrap

ci_dir = Path(__file__).parent
root = ci_dir.parent
action_file = root / "action.yml"
readme = root / "README.md"
template = ci_dir / "README.template.md"


def get_inputs() -> str:
    raw = action_file.read_text()
    return textwrap.dedent(raw.split("inputs:")[1].split("runs:")[0]).strip()


def main():
    readme.write_text(
        template.read_text(encoding="UTF-8").format(input_ref=get_inputs())
    )


if __name__ == "__main__":
    main()
