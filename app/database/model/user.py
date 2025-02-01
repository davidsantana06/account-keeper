from sqlalchemy import Column, Integer, String
from app.extension import database
from ..inheritable import Model, TimestampMixin


class User(database.Model, Model, TimestampMixin):
    id = Column(Integer, autoincrement=True, primary_key=True)

    # identification  _
    name = Column(String, nullable=False)

    # preference _
    first_view = Column(String, nullable=False)
    password_complexity = Column(String, nullable=False)
    zoom = Column(String, nullable=False)

    @classmethod
    def find_first(cls) -> "User":
        return cls._query_first(filters={cls.id == 1})
