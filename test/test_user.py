from flask import Flask
from pytest import fixture
from random import choice
from werkzeug.datastructures import MultiDict

from app.facade import Password
from app.form import UserForm
from app.service import UserService


_DATA = {
    "name": ["Aquila", "César Augusto", "Silas", "Tertuliano"],
    "first_view": ["home:index", "account:index"],
    "password_complexity": [
        Password.LOW_COMPLEXITY,
        Password.MEDIUM_COMPLEXITY,
        Password.HIGH_COMPLEXITY,
    ],
    "zoom": [f"zoom-{i}" for i in range(6)],
}


@fixture
def data():
    return MultiDict({key: choice(values) for key, values in _DATA.items()})


def test_create(app: Flask):
    with app.app_context():
        assert UserService.get() is None
        user = UserService.create_if_absent()
        assert user.id == 1
        assert user.name in [
            "Águia Viajante",
            "Cavalo Desbravador",
            "Cão Caçador",
            "Galo Pioneiro",
            "Leão Nômade",
            "Ovelha Viajante",
            "Pato Explorador",
        ]
        assert user.first_view == "home:index"
        assert user.password_complexity == Password.LOW_COMPLEXITY
        assert user.zoom == "zoom-0"


def test_get(app: Flask):
    with app.app_context():
        user = UserService.get()
        assert user.id == 1


def test_fill(app: Flask):
    with app.app_context():
        form = UserForm()
        user = UserService.fill(form)
        assert form.name.data == user.name
        assert form.first_view.data == user.first_view
        assert form.password_complexity.data == user.password_complexity
        assert form.zoom.data == user.zoom


def test_update(app: Flask, data: MultiDict):
    with app.app_context():
        form = UserForm(data)
        user = UserService.update(form)
        assert user.id == 1
        assert user.name == data["name"]
        assert user.first_view == data["first_view"]
        assert user.password_complexity == data["password_complexity"]
        assert user.zoom == data["zoom"]
