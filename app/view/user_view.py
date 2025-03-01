from flask_classful import FlaskView
from app.facade import ResponseFacade


class UserView(FlaskView):
    def index(self):
        return ResponseFacade.as_page("user:index")

    def update(self):
        return ""
