from typer import Typer
from .module.account import account


app = Typer()
app.add_typer(account, name='account')
