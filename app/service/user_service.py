from random import choice

from app.database import User
from app.form import UserForm


class UserService:
    _ZOOM_CHOICES = [
        ("zoom-0", "Pé no Chão (100%)"),
        ("zoom-1", "Horizonte Próximo (110%)"),
        ("zoom-2", "Alcance Amplo (120%)"),
        ("zoom-3", "Foco Cirúrgico (130%)"),
        ("zoom-4", "Perspectiva de Águia (140%)"),
        ("zoom-5", "Panorama Celestial (150%)"),
    ]

    @staticmethod
    def _choice_name() -> str:
        return choice(
            [
                "Arara Viajante",
                "Gavião Desbravador",
                "Jaguar Caçador",
                "Lobo Pioneiro",
                "Sabiá Nômade",
                "Tatu Viajante",
                "Tucano Explorador",
            ]
        )

    @classmethod
    def create(cls) -> User:
        user = User()
        user.name = cls._choice_name()
        user.zoom = cls._ZOOM_CHOICES[0][1]
        User.save(user)
        return user

    @staticmethod
    def get() -> User:
        return User.find_first()

    @classmethod
    def fill(cls, form: UserForm) -> None:
        user = cls.get()
        form.zoom.choices = cls._ZOOM_CHOICES
        form.process(obj=user)

    @classmethod
    def update(cls, form: UserForm) -> None:
        user = cls.get()
        form.populate_obj(user)
        User.save(user)
