__version__ = "0.2.0"


from flask import Flask
from .config import Setup


app = Flask(__name__)
Setup.apply_parameters(app)
Setup.initialize_extensions(app)
Setup.create_tables(app)
Setup.register_views(app)
Setup.inject_jinja_globals(app)
