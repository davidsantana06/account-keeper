from flask import request
from flask_classful import FlaskView, route

from app.facade import Flash, Response, Url
from app.form import AccountForm
from app.service import AccountService


class AccountView(FlaskView):
    def index(self):
        search = request.args.get("search", "")
        accounts = AccountService.get_all(search)
        return Response.as_page("account:index", {"accounts": accounts})

    def create(self):
        form = AccountForm()
        return Response.as_page("account:create", {"form": form})

    def post(self):
        form = AccountForm(request.form)
        account = AccountService.create(form)
        Flash.append("Conta adicionada ao catálogo", "success")
        return Response.as_redirect(Url.for_view("account:update", id=account.id))

    def update(self, id: int):
        form = AccountForm()
        account = AccountService.fill(id, form)
        return Response.as_page("account:update", {"account": account, "form": form})

    @route("/put/<int:id>", methods=["POST"])
    def put(self, id: int):
        form = AccountForm(request.form)
        AccountService.update(id, form)
        Flash.append("Conta atualizada", "info")
        return Response.as_redirect(Url.for_view("account:update", id=id))

    @route("/generate-password/<int:id>", methods=["GET"])
    def generate_password(self, id: int):
        AccountService.generate_password(id)
        Flash.append("Senha atualizada", "info")
        return Response.as_redirect(Url.for_view("account:update", id=id))

    @route("/delete/<int:id>", methods=["GET"])
    def delete(self, id: int):
        AccountService.delete(id)
        Flash.append("Conta excluída do catálogo", "info")
        return Response.as_redirect(Url.for_view("account:index"))
