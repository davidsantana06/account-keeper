from app.database import Account, Accounts
from app.facade import PasswordFacade
from app.form import AccountForm

from .user_service import UserService


class AccountService:
    @staticmethod
    def create(form: AccountForm) -> Account:
        account = Account()
        form.populate_obj(account)
        Account.save(account)
        return account

    @staticmethod
    def get_all(search: str = "") -> Accounts:
        return Account.find_all(search)

    @staticmethod
    def get_one_by_id(id: int) -> Account:
        return Account.find_first_by_id(id)

    @classmethod
    def fill(cls, id: int, form: AccountForm) -> Account:
        account = cls.get_one_by_id(id)
        form.process(obj=account)
        return account

    @classmethod
    def update(cls, id: int, form: AccountForm) -> Account:
        account = cls.get_one_by_id(id)
        form.populate_obj(account)
        Account.save(account)
        return account

    @classmethod
    def generate_password(cls, id: int) -> Account:
        user = UserService.get()
        account = cls.get_one_by_id(id)
        account.password = PasswordFacade.generate(user.password_complexity)
        Account.save(account)
        return account

    @classmethod
    def delete(cls, id: int) -> Account:
        account = cls.get_one_by_id(id)
        Account.delete(account)
        return account
