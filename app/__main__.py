from flask import Flask
from .config import Setup


if __name__ == "__main__":
    app = Flask(__name__)

    Setup.apply_parameters(app)
    Setup.create_storage_dir()
    Setup.initialize_database(app)
    Setup.create_user(app)
    Setup.register_views(app)
    Setup.inject_jinja_globals(app)

    app.run(debug=True)
