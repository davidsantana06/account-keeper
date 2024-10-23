from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from typing import List

from .base import Base


Accounts = List['Account']


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String)
    email = Column(String)
    phone = Column(String)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.now(),
        onupdate=datetime.now()
    )

    @classmethod
    def _query_all(cls, filters: List = None) -> Accounts:
        return super()._query_all(
            filters=filters,
            ordinances=[cls.name, cls.created_at]
        )

    @classmethod
    def find_all(cls) -> Accounts:
        return cls._query_all()

    @classmethod
    def find_all_by_name(cls, name: str) -> Accounts:
        return cls._query_all(filters=[cls.name.icontains(name)])

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Account':
        return cls._query_first(filters=[cls.id == id])

    @classmethod
    def find_first_by_name(cls, name: str) -> 'Account':
        return cls._query_first(filters=[cls.name.ilike(name)])

    def __init__(
        self,
        name: str,
        username: str,
        email: str,
        phone: str,
        password: str
    ) -> None:
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password
