from pathlib import Path

ci_dir = Path(__file__).parent
template_file = ci_dir / "input_template.md"


class Input:
    def __init__(
        self, name: str, description: str, required: bool, default: str
    ) -> None:
        self.name = name
        self.description = description
        self.required = required
        self.default = default

    @property
    def human_readable_required(self) -> str:
        return str(self.required).lower()

    @property
    def type(self) -> str:
        if self.default in ("false", "true"):
            return "bool"
        return "str"

    def formatted(self) -> str:
        return template_file.read_text().format(inp=self)
