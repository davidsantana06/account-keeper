from dotenv import load_dotenv
from flask import Flask
from http import HTTPStatus
from werkzeug.exceptions import HTTPException

from app.extension import db
from app.facade import Flash, Response, Url, View
from app.service import UserService
from app.view import AccountView, HomeView, UserView

from .parameter import Parameter
from .path import Path


class Setup:
    @staticmethod
    def apply_parameters(app: Flask) -> None:
        load_dotenv(Path.ENV_FILE, override=True)
        app.config.from_object(Parameter)
        app.static_folder = Path.STATIC_FOLDER
        app.template_folder = Path.TEMPLATE_FOLDER

    @staticmethod
    def init_database(app: Flask) -> None:
        db.init_app(app)
        with app.app_context():
            db.create_all()

    @staticmethod
    def create_user(app: Flask) -> None:
        with app.app_context():
            UserService.create_if_absent()

    @staticmethod
    def register_views(app: Flask) -> None:
        AccountView.register(app)
        HomeView.register(app, route_base="/")
        UserView.register(app)

    @staticmethod
    def __handle_error(_: Exception):
        Flash.append("Erro — O destino conspirou contra esta operação", "danger")
        user = UserService.get()
        return Response.as_redirect(Url.for_view(user.first_view))

    @classmethod
    def register_error_handlers(cls, app: Flask) -> None:
        app.register_error_handler(Exception, cls.__handle_error)

    @staticmethod
    def inject_jinja_globals(app: Flask) -> None:
        app.context_processor(
            lambda: {
                "layout": (lambda layout: View.resolve(f"layout/{layout}")),
                "macro": (lambda macro: View.resolve(f"macro/{macro}")),
                "partial": (lambda partial: View.resolve(f"partial/{partial}")),
                "static": Url.for_static,
                "view": Url.for_view,
                "flashes": Flash.pop_all(),
                "user": UserService.get(),
            }
        )
