from flask import Flask
from os import makedirs

from app.database import *
from app.extension import database
from app.facade import FlashFacade, TemplateFacade, URLFacade
from app.view import HomeView

from .parameter import Parameter
from .path import Path


class Setup:
    @staticmethod
    def apply_parameters(app: Flask) -> None:
        app.config.from_object(Parameter)
        app.static_folder = Path.STATIC_DIR
        app.template_folder = Path.TEMPLATE_DIR

    @staticmethod
    def create_storage_dir() -> None:
        makedirs(Path.STORAGE_DIR, exist_ok=True)

    @staticmethod
    def initialize_database(app: Flask) -> None:
        database.init_app(app)
        with app.app_context():
            database.create_all()

    @staticmethod
    def create_user(app: Flask) -> None:
        with app.app_context(): ...

    @staticmethod
    def register_views(app: Flask) -> None:
        HomeView.register(app)

    @staticmethod
    def inject_jinja_globals(app: Flask) -> None:
        app.context_processor(
            lambda: {
                "fragment": (
                    lambda fragment: TemplateFacade.resolve(f"fragment/{fragment}")
                ),
                "layout": (lambda layout: TemplateFacade.resolve(f"layout/{layout}")),
                "macro": (lambda macro: TemplateFacade.resolve(f"macro/{macro}")),
                "static": URLFacade.for_static,
                "view": URLFacade.for_view,
                "flashes": FlashFacade.pop_all(),
            }
        )
