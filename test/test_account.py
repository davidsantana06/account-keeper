from flask import Flask
from pytest import fixture, mark
from pytest_mock import MockerFixture
from random import choice
from werkzeug.datastructures import MultiDict

from app.database import User
from app.form import AccountForm
from app.service import AccountService


_DATA = {
    "name": [
        "GitHub",
        "Google",
        "PSN",
        "Steam",
        "Facebook",
        "Twitter",
        "LinkedIn",
        "Instagram",
    ],
    "category": [
        "bronze",
        "silver",
        "gold",
    ],
    "notes": [
        "",
        "Atualizar a senha a cada 15 dias",
        "Mudar a foto de perfil",
        "Ativar autenticação em dois fatores",
        "Conta compartilhada com equipe",
        "Evitar login em redes públicas",
    ],
    "username": [
        "",
        "user77",
        "admin2025",
        "johndoe",
        "supergamer99",
        "tech_guru",
        "darkwolf",
        "coderx",
    ],
    "email": [
        "",
        "user@example.com",
        "admin@domain.com",
        "contact@website.org",
        "hello@service.net",
        "gaming@play.com",
        "security@safe.com",
    ],
    "phone": [
        "",
        "(11) 90000-0000",
        "(21) 90000-0000",
        "(31) 90000-0000",
        "(41) 98888-7777",
        "(51) 97777-6666",
        "(61) 96666-5555",
    ],
    "password": [
        "securepassword123",
        "mypassword",
        "123456",
        "qwerty789",
        "P@ssw0rd!",
        "letmein2024",
        "hunter2",
        "superSecurePass!",
    ],
}


@fixture
def data():
    return MultiDict({key: choice(values) for key, values in _DATA.items()})


@mark.loop(10)
def test_create(app: Flask, data: MultiDict):
    with app.app_context():
        form = AccountForm(data)
        account = AccountService.create(form)
        assert account.name == data["name"]
        assert account.notes == data["notes"]
        assert account.username == data["username"]
        assert account.email == data["email"]
        assert account.phone == data["phone"]
        assert account.password == data["password"]


def test_get_all(app: Flask):
    with app.app_context():
        accounts = AccountService.get_all()
        assert len(accounts) == 10


def test_get_one_by_id(app: Flask):
    with app.app_context():
        account = AccountService.get_one_by_id(2)
        assert account.id == 2


def test_fill(app: Flask):
    with app.app_context():
        form = AccountForm()
        account = AccountService.fill(4, form)
        assert account.id == 4
        assert form.name.data == account.name
        assert form.notes.data == account.notes
        assert form.username.data == account.username
        assert form.email.data == account.email
        assert form.phone.data == account.phone
        assert form.password.data == account.password


def test_update(app: Flask, data: MultiDict):
    with app.app_context():
        form = AccountForm(data)
        account = AccountService.update(6, form)
        assert account.id == 6
        assert account.name == data["name"]
        assert account.notes == data["notes"]
        assert account.username == data["username"]
        assert account.email == data["email"]
        assert account.phone == data["phone"]
        assert account.password == data["password"]


def test_generate_password(app: Flask, mocker: MockerFixture):
    mocker.patch(
        "app.service.user_service.UserService.get",
        return_value=User(),
    )
    mocker.patch("app.facade.password.Password.generate", return_value="password77")
    with app.app_context():
        AccountService.generate_password(8)
        account = AccountService.get_one_by_id(8)
        assert account.password == "password77"


def test_delete(app: Flask):
    with app.app_context():
        account = AccountService.delete(10)
        assert account.id == 10
