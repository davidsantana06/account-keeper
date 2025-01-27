from flask_classful import FlaskView


class HomeView(FlaskView):
    route_base = '/'

    def index(self):
        return '...'
