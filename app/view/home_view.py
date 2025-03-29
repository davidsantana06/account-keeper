from flask import session
from flask_classful import FlaskView

from app.facade import ResponseFacade, URLFacade
from app.service import UserService


class HomeView(FlaskView):
    def before_request(self, _: str):
        is_first_acess = "first_acess" not in session
        if is_first_acess:
            session["first_acess"] = False
            user = UserService.get()
            return ResponseFacade.as_redirect(URLFacade.for_view(user.first_view))

    def index(self):
        return ResponseFacade.as_page("home:index")
