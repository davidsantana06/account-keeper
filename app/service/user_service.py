from app.database import User
from app.form import UserForm


class UserService:
    @classmethod
    def create_if_absent(cls) -> User:
        user = cls.get()
        if not user:
            user = User()
            User.save(user)
        return user

    @staticmethod
    def get() -> User:
        return User.find_first()

    @classmethod
    def fill(cls, form: UserForm) -> User:
        user = cls.get()
        form.process(obj=user)
        return user

    @classmethod
    def update(cls, form: UserForm) -> User:
        user = cls.get()
        form.populate_obj(user)
        User.save(user)
        return user
