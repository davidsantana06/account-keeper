from typing import List, Literal, Union

from app.database import Account, Accounts
from app.facade import password_facade


def create(*data: List[str]) -> Account:
    password = password_facade.generate('medium')
    account = Account(*data, password)
    Account.save(account)
    return account

def get_all() -> Accounts:
    return Account.find_all()


def get_all_by_name(name: str) -> Accounts:
    return Account.find_all_by_name(name)


def get_first_by(
    field: Literal['id', 'name'],
    value: Union[int, str]
) -> Account:
    function = getattr(Account, f'find_first_by_{field}')
    return function(value)


def _update(
    account: Account,
    field: Literal['name', 'password'],
    value: str
) -> Account:
    setattr(account, field, value)
    Account.save(account)
    return account


def update_name(account: Account, name: str) -> Account:
    return _update(account, 'name', name)


def update_password(
    account: Account,
    level: password_facade.Level
) -> Account:
    password = password_facade.generate(level)
    return _update(account, 'password', password)


def delete(account: Account) -> None:
    Account.delete(account)
