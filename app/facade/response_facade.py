from flask import Response, redirect
from .view_facade import ViewFacade


class ResponseFacade:
    @staticmethod
    def as_page(template: str, context: dict[str, object] | None = None) -> Response:
        folder, filename = template.split(":")
        return ViewFacade.render(f"page/{folder}/{filename}", context)

    @staticmethod
    def as_redirect(location: str) -> Response:
        return redirect(location)
