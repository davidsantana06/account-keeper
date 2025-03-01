from flask_classful import FlaskView

from app.facade import ResponseFacade
from app.service import AccountService


class AccountView(FlaskView):
    def index(self):
        accounts = AccountService.get_all()
        return ResponseFacade.as_page("account:index", {"accounts": accounts})

    def create(self):
        return ""

    def update(self, id: int):
        return ""
