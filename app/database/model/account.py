from sqlalchemy import Column, Integer, String, or_
from app.extension import db
from ..base import Model, TimestampMixin


Accounts = list["Account"]


class Account(db.Model, Model, TimestampMixin):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    notes = Column(String)
    username = Column(String)
    email = Column(String)
    phone = Column(String)
    password = Column(String)

    @classmethod
    def find_all(cls, search: str) -> Accounts:
        return (
            cls.query.filter(
                or_(
                    cls.name.icontains(search),
                    cls.notes.icontains(search),
                    cls.username.icontains(search),
                    cls.email.icontains(search),
                    cls.phone.icontains(search),
                )
            )
            .order_by(
                cls.name,
                cls.username,
                cls.email,
                cls.phone,
            )
            .all()
        )

    @classmethod
    def find_first_by_id(cls, id: int) -> "Account":
        return cls.query.filter(cls.id == id).first()

    @property
    def group(self) -> str:
        char = self.name[0].lower()
        is_letter = "a" <= char <= "z"
        return char if is_letter else "#"
