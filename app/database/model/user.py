from sqlalchemy import Column, Integer, String
from app.extension import database
from ..inheritable import Model, TimestampMixin


class User(database.Model, Model, TimestampMixin):
    id = Column(Integer, autoincrement=True, primary_key=True)

    # basic  _
    name = Column(String, nullable=False)

    # preference _
    zoom = Column(String, nullable=False)

    @classmethod
    def find_first(cls) -> 'User':
        return cls._query_first(filters={cls.id == 1})
