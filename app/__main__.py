from . import app
from .config.setup import create_database, create_storage_dir


if __name__ == '__main__':
    create_storage_dir()
    create_database()
    app()
