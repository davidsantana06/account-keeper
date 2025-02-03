from flask import Flask
import webview

from app.database import *
from app.extension import database
from app.facade import FlashFacade, TemplateFacade, URLFacade
from app.service import UserService
from app.view import AccountView, HomeView, UserView

from .parameter import Parameter
from .path import Path


class Setup:
    @staticmethod
    def apply_parameters(app: Flask) -> None:
        app.config.from_object(Parameter)
        app.static_folder = Path.STATIC_DIR
        app.template_folder = Path.TEMPLATE_DIR

    @staticmethod
    def initialize_database(app: Flask) -> None:
        database.init_app(app)
        with app.app_context():
            database.create_all()

    @staticmethod
    def create_user(app: Flask) -> None:
        with app.app_context():
            user = UserService.get()
            if not user:
                UserService.create()

    @staticmethod
    def register_views(app: Flask) -> None:
        AccountView.register(app)
        HomeView.register(app)
        UserView.register(app)

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
                "user": UserService.get(),
            }
        )

    @staticmethod
    def open_window(app: Flask) -> None:
        webview.create_window("Account Keeper", app, min_size=(500, 500))
        webview.start(icon=Path.ICON_FILE)
