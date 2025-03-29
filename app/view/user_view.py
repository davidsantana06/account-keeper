from flask import request
from flask_classful import FlaskView, route

from app.facade import FlashFacade, ResponseFacade, URLFacade
from app.form import UserForm
from app.service import UserService


class UserView(FlaskView):
    def index(self):
        return ResponseFacade.as_page("user:index")

    def update(self):
        form = UserForm()
        UserService.fill(form)
        return ResponseFacade.as_page("user:update", {"form": form})

    @route("/put", methods=["POST"])
    def put(self):
        form = UserForm(request.form)
        UserService.update(form)
        FlashFacade.append("Perfil atualizado", "info")
        return ResponseFacade.as_redirect(URLFacade.for_view("user:update"))
