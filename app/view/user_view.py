from flask import request
from flask_classful import FlaskView, route

from app.facade import Flash, Response, Url
from app.form import UserForm
from app.service import UserService


class UserView(FlaskView):
    def index(self):
        return Response.as_page("user:index")

    def update(self):
        form = UserForm()
        UserService.fill(form)
        return Response.as_page("user:update", {"form": form})

    @route("/put", methods=["POST"])
    def put(self):
        form = UserForm(request.form)
        UserService.update(form)
        Flash.append("Perfil atualizado", "info")
        return Response.as_redirect(Url.for_view("user:update"))
