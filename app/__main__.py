from flask import Flask
from .config import Setup


if __name__ == "__main__":
    app = Flask(__name__)

    Setup.apply_parameters(app)
    Setup.initialize_database(app)
    Setup.create_user(app)
    Setup.register_views(app)
    Setup.inject_jinja_globals(app)
    Setup.open_window(app)
