from app import database
from . import path


def create_storage_dir() -> None:
    path.STORAGE_DIR.mkdir(exist_ok=True)


def create_database() -> None:
    database.create_all()
