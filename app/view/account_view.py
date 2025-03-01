from flask import request
from flask_classful import FlaskView

from app.facade import FlashFacade, ResponseFacade, URLFacade
from app.form import AccountForm
from app.service import AccountService


class AccountView(FlaskView):
    def index(self):
        accounts = AccountService.get_all()
        return ResponseFacade.as_page("account:index", {"accounts": accounts})

    def create(self):
        form = AccountForm()
        return ResponseFacade.as_page("account:create", {"form": form})

    def post(self):
        form = AccountForm(request.form)
        account = AccountService.create(form)
        FlashFacade.append("A conta foi adicionada ao catálogo", "success")
        return ResponseFacade.as_async_redirect(
            URLFacade.for_view("account:update", id=account.id)
        )

    def update(self, id: int):
        return ""
