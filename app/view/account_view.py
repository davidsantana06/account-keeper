from flask import request
from flask_classful import FlaskView, route

from app.facade import FlashFacade, ResponseFacade, URLFacade
from app.form import AccountForm
from app.service import AccountService


class AccountView(FlaskView):
    def index(self):
        search = request.args.get("search", "")
        accounts = AccountService.get_all(search)
        return ResponseFacade.as_page("account:index", {"accounts": accounts})

    def create(self):
        form = AccountForm()
        return ResponseFacade.as_page("account:create", {"form": form})

    def post(self):
        form = AccountForm(request.form)
        account = AccountService.create(form)
        FlashFacade.append("Conta adicionada ao catálogo", "success")
        return ResponseFacade.as_redirect(
            URLFacade.for_view("account:update", id=account.id)
        )

    def update(self, id: int):
        form = AccountForm()
        account = AccountService.fill(id, form)
        return ResponseFacade.as_page(
            "account:update", {"account": account, "form": form}
        )

    @route("/put/<int:id>", methods=["POST"])
    def put(self, id: int):
        form = AccountForm(request.form)
        AccountService.update(id, form)
        FlashFacade.append("Conta atualizada", "info")
        return ResponseFacade.as_redirect(URLFacade.for_view("account:update", id=id))

    @route("/generate-password/<int:id>", methods=["GET"])
    def generate_password(self, id: int):
        AccountService.generate_password(id)
        FlashFacade.append("Senha atualizada", "info")
        return ResponseFacade.as_redirect(URLFacade.for_view("account:update", id=id))

    @route("/delete/<int:id>", methods=["GET"])
    def delete(self, id: int):
        AccountService.delete(id)
        FlashFacade.append("Conta excluída do catálogo", "info")
        return ResponseFacade.as_redirect(URLFacade.for_view("account:index"))
