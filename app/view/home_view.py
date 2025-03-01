from flask_classful import FlaskView
from app.facade import ResponseFacade


class HomeView(FlaskView):
    route_base = "/"

    def index(self):
        return ResponseFacade.as_page("home:index")
