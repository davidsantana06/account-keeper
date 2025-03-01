from flask import render_template


class ViewFacade:
    @staticmethod
    def resolve(template: str) -> str:
        return f"{template}.html.j2"

    @classmethod
    def render(cls, template: str, context: dict[str, object] | None = None) -> str:
        return render_template(cls.resolve(template), **(context or {}))
