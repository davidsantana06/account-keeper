from flask import request
from flask_classful import FlaskView

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

    def put(self):
        form = UserForm(request.form)
        UserService.update(form)
        FlashFacade.append("O perfil foi atualizado", "info")
        return ResponseFacade.as_async_redirect(URLFacade.for_view("user:index"))
