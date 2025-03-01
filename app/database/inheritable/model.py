from flask_sqlalchemy.model import Model as SQLAlchemyModel
from app.extension import db


class Model(SQLAlchemyModel):
    @staticmethod
    def save(model: "Model") -> None:
        db.session.add(model)
        db.session.commit()

    @staticmethod
    def delete(model: "Model") -> None:
        db.session.delete(model)
        db.session.commit()

    @classmethod
    def _query_all(cls, order_by: list | None = None) -> list["Model"]:
        query = cls.query
        if order_by: query = query.order_by(*order_by)
        return query.all()

    @classmethod
    def _query_first(cls, filters: list) -> "Model":
        return cls.query.filter(*filters).first()
