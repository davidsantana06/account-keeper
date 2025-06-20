from os import environ
from .path import Path


class Parameter:
    PORT = int(environ.get("PORT", "5000"))

    SECRET_KEY = "Account Keeper _ by davidsantana06"

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path.DATABASE_FILE}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = False
