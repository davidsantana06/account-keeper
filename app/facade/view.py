from flask import render_template


class View:
    @staticmethod
    def resolve(template: str) -> str:
        return f"{template}.html.j2"

    @classmethod
    def render(
        cls,
        template: str,
        context: dict[str, object] | None,
    ) -> str:
        return render_template(cls.resolve(template), **(context or {}))
