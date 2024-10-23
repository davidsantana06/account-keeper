from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from typing import List

from app.config import path


def _create_engine() -> Engine:
    return create_engine(f'sqlite:///{path.DATABASE_FILE}')


def _make_session(engine: Engine) -> Session:
    return sessionmaker(engine)()


_engine = _create_engine()
_session = _make_session(_engine)


class Base(DeclarativeBase):
    __abstract__ = True

    @staticmethod
    def save(model: 'Base') -> None:
        try:
            _session.add(model)
            _session.commit()
        except Exception as e:
            _session.rollback()
            raise e

    @staticmethod
    def delete(model: 'Base') -> None:
        try:
            _session.delete(model)
            _session.commit()
        except Exception as e:
            _session.rollback()
            raise e

    @classmethod
    def _query_all(
        cls,
        filters: List = None,
        ordinances: List = None
    ) -> List['Base']:
        query = _session.query(cls)
        if filters: query = query.filter(*filters)
        if ordinances: query = query.order_by(*ordinances)
        return query.all()

    @classmethod
    def _query_first(cls, filters: List = None) -> 'Base':
        query = _session.query(cls)
        if filters: query = query.filter(*filters)
        return query.first()


def create_all() -> None:
    Base.metadata.create_all(_engine)


def drop_all() -> None:
    Base.metadata.drop_all(_engine)
