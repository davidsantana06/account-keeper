from random import choice
from sqlalchemy import Column, Integer, String

from app.extension import db
from app.facade import Password

from ..base import Model, TimestampMixin


class User(db.Model, Model, TimestampMixin):
    id = Column(Integer, autoincrement=True, primary_key=True)

    # identification  _
    name = Column(
        String,
        nullable=False,
        default=choice(
            [
                "Águia Viajante",
                "Cavalo Desbravador",
                "Cão Caçador",
                "Galo Pioneiro",
                "Leão Nômade",
                "Ovelha Viajante",
                "Pato Explorador",
            ]
        ),
    )

    # preference _
    first_view = Column(String, nullable=False, default="home:index")
    password_complexity = Column(
        String, nullable=False, default=Password.LOW_COMPLEXITY
    )
    zoom = Column(String, nullable=False, default="zoom-0")

    @classmethod
    def find_first(cls) -> "User":
        return cls.query.filter(cls.id == 1).first()
