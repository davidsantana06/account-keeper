from datetime import datetime
from flask import Flask
from pytest import fixture
from os import path

from app.extension import db


@fixture
def app():
    current_date = datetime.now().strftime("%Y-%m-%d")
    database_file = path.join(path.dirname(__file__), f"{current_date}.sqlite3")

    app_ = Flask(__name__)
    app_.config.from_mapping(
        {
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{database_file}",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
            "TESTING": True,
            "WTF_CSRF_ENABLED": False,
        }
    )

    db.init_app(app_)
    with app_.app_context():
        db.create_all()

    return app_
