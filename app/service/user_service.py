from random import choice

from app.database import User
from app.facade import PasswordFacade
from app.form import UserForm


class UserService:
    _PASSWORD_COMPLEXITY_CHOICES = [
        (PasswordFacade.LOW_COMPLEXITY, "Levis (Baixa)"),
        (PasswordFacade.MEDIUM_COMPLEXITY, "Modicus (Média)"),
        (PasswordFacade.HIGH_COMPLEXITY, "Perplexus (Alta)"),
    ]

    _ZOOM_CHOICES = [
        ("zoom-0", "Pé no Solo (100%)"),
        ("zoom-1", "Vista do Fórum (110%)"),
        ("zoom-2", "Olhar do Legado (120%)"),
        ("zoom-3", "Visão do Centurião (130%)"),
        ("zoom-4", "Olho de Júpiter (140%)"),
        ("zoom-5", "Horizonte do Coliseu (150%)"),
    ]

    @staticmethod
    def _choice_name() -> str:
        return choice(
            [
                "Águia Viajante",
                "Cavalo Desbravador",
                "Cão Caçador",
                "Galo Pioneiro",
                "Leão Nômade",
                "Ovelha Viajante",
                "Pato Explorador",
            ]
        )

    @classmethod
    def create(cls) -> User:
        user = User()
        user.name = cls._choice_name()
        user.password_complexity = cls._PASSWORD_COMPLEXITY_CHOICES[0][0]
        user.zoom = cls._ZOOM_CHOICES[0][0]
        User.save(user)
        return user

    @staticmethod
    def get() -> User:
        return User.find_first()

    @classmethod
    def fill(cls, form: UserForm) -> None:
        user = cls.get()
        form.password_complexity.choices = cls._PASSWORD_COMPLEXITY_CHOICES
        form.zoom.choices = cls._ZOOM_CHOICES
        form.process(obj=user)

    @classmethod
    def update(cls, form: UserForm) -> None:
        user = cls.get()
        form.populate_obj(user)
        User.save(user)
