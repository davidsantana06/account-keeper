from flask import Response, jsonify, redirect
from .template_facade import TemplateFacade


class ResponseFacade:
    @staticmethod
    def as_page(template: str, context: dict[str, object] | None = None) -> Response:
        folder, file_name = template.split(":")
        return TemplateFacade.render(f"page/{folder}/{file_name}", context)

    @staticmethod
    def as_async_redirect(location: str) -> Response:
        return jsonify({"redirect": location})

    @staticmethod
    def as_sync_redirect(location: str) -> Response:
        return redirect(location)
