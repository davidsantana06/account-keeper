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
    def _query_all(cls, ordinances: set | None = None) -> list["Model"]:
        query = cls.query
        if ordinances:
            query = query.order_by(*ordinances)
        return query.all()

    @classmethod
    def _query_first(cls, filters: set) -> "Model":
        return cls.query.filter(*filters).first()
