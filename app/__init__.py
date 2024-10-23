from typer import Typer
from .config import create_storage_dir, create_database


create_storage_dir()
create_database()

app = Typer()
