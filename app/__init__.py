__version__ = "0.5.0"


from flask import Flask
from .config import Setup


app = Flask(__name__)
Setup.apply_parameters(app)
Setup.init_database(app)
Setup.create_user(app)
Setup.register_views(app)
Setup.register_error_handlers(app)
Setup.inject_jinja_globals(app)
