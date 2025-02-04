from app.database import User
from app.form import UserForm


class UserService:
    @classmethod
    def create(cls) -> None:
        user = cls.get()
        if not user:
            user = User()
            User.save(user)

    @staticmethod
    def get() -> User:
        return User.find_first()

    @classmethod
    def fill(cls, form: UserForm) -> None:
        user = cls.get()
        form.process(obj=user)

    @classmethod
    def update(cls, form: UserForm) -> None:
        user = cls.get()
        form.populate_obj(user)
        User.save(user)
