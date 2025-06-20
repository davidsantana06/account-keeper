from flask import url_for


class Url:
    @staticmethod
    def for_static(endpoint: str) -> str:
        folder, filename = endpoint.split(":")
        folder = f"{folder}/" if folder != "root" else ""
        return url_for("static", filename=f"{folder}{filename}")

    @staticmethod
    def for_view(endpoint: str, **values: object) -> str:
        module, method = endpoint.split(":")
        class_ = module.capitalize() + "View"
        return url_for(f"{class_}:{method}", **values)
