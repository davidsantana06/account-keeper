from flask import Flask

from app.extension import db
from app.facade import FlashFacade, URLFacade, ViewFacade

from .parameter import Parameter
from .path import Path


class Setup:
    @staticmethod
    def apply_parameters(app: Flask) -> None:
        app.config.from_object(Parameter)
        app.static_folder = Path.STATIC_FOLDER
        app.template_folder = Path.TEMPLATE_FOLDER

    @staticmethod
    def init_database(app: Flask) -> None:
        db.init_app(app)
        with app.app_context():
            db.create_all()

    @staticmethod
    def create_user(app: Flask) -> None: ...

    @staticmethod
    def register_views(app: Flask) -> None: ...

    @staticmethod
    def inject_jinja_globals(app: Flask) -> None:
        app.context_processor(
            lambda: {
                "layout": (lambda layout: ViewFacade.resolve(f"layout/{layout}")),
                "macro": (lambda macro: ViewFacade.resolve(f"macro/{macro}")),
                "partial": (lambda partial: ViewFacade.resolve(f"partial/{partial}")),
                "static": URLFacade.for_static,
                "view": URLFacade.for_view,
                "flashes": FlashFacade.pop_all(),
            }
        )
