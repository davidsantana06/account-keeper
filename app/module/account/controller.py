from typer import echo, Option
from typing import Optional

from app.facade import password_facade
from . import account_operation, account


@account.command()
def create(
    name: str,
    username: str = None,
    email: str = None,
    phone: str = None
):
    account = account_operation.create(name, username, email, phone)
    echo(f'Account created with password {account.password}')


@account.command()
def all(
    name: Optional[str] = Option(None, '--name', case_sensitive=False)
):
    accounts = (
        account_operation.get_all_by_name(name)
        if name else account_operation.get_all()
    )
    if accounts: echo('Accounts found:')
    for account in accounts: echo(f'#{account.id} {account.name}')


@account.command()
def one(
    id: Optional[int] = Option(None, '--id', case_sensitive=False),
    name: Optional[str] = Option(None, '--name', case_sensitive=False)
):
    field, value = ('id', id) if id else ('name', name)
    account = account_operation.get_first_by(field, value)
    if account: 
        echo(
            f'Account #{account.id}: \n'
            f'* Name: {account.name}, \n'
            f'* Username: {account.username}, \n'
            f'* E-mail: {account.email}, \n'
            f'* Phone: {account.phone}, \n'
            f'* Password: {account.password}'
        )


@account.command()
def update(
    id: int,
    name: Optional[str] = Option(None, '--name', case_sensitive=False),
    password: bool = Option(False, '--password', case_sensitive=False),
    level: Optional[str] = Option(
        password_facade.MEDIUM, 
        '--level', 
        case_sensitive=False
    )
):
    account = account_operation.get_first_by('id', id)
    if account:
        if name:
            account = account_operation.update_name(account, name)
            echo(f'Name updated to {account.name}.')
        if password:
            account = account_operation.update_password(
                account,
                level
            )
            echo(f'Password updated to {account.password}.')


@account.command()
def delete(id: int):
    account = account_operation.get_first_by('id', id)
    if account:
        account_operation.delete(account)
        echo('Account deleted.')
