from sqlalchemy import Column, Integer, String
from app.extension import db
from ..inheritable import Model, TimestampMixin


Accounts = list["Account"]


class Account(db.Model, Model, TimestampMixin):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False, server_default="Comum")
    notes = Column(String)
    username = Column(String)
    email = Column(String)
    phone = Column(String)
    password = Column(String)

    @classmethod
    def find_all(cls) -> Accounts:
        return cls._query_all(
            order_by=[
                cls.name,
                cls.username,
                cls.email,
                cls.phone,
                cls.category.desc(),
            ]
        )

    @classmethod
    def find_first_by_id(cls, id: int) -> "Account":
        return cls._query_first(filters={cls.id == id})

    @property
    def group(self) -> str:
        char = self.name[0].lower()
        is_letter = "a" <= char <= "z"
        return char if is_letter else "#"

    @property
    def category_class(self) -> str:
        return {"Comum": "dark", "Especial": "white"}[self.category]
