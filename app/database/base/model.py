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
