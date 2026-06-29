from sqlalchemy.orm import Session

from backend.auth.security import (
    hash_password,
    verify_password,
    create_access_token
)

from backend.models.user import User
from backend.repositories.user_repository import UserRepository
from backend.schemas.user import UserRegister, UserLogin


class AuthHandler:

    @staticmethod
    def register(db: Session, user: UserRegister):

        if UserRepository.get_by_email(db, user.email):
            raise ValueError("Email already registered.")

        if UserRepository.get_by_username(db, user.username):
            raise ValueError("Username already exists.")

        new_user = User(
            username=user.username,
            email=user.email,
            password=hash_password(user.password),
            role="analyst"
        )

        return UserRepository.create(db, new_user)

    @staticmethod
    def login(db: Session, user: UserLogin):

        db_user = UserRepository.get_by_email(
            db,
            user.email
        )

        if not db_user:
            raise ValueError("Invalid email or password.")

        if not verify_password(
            user.password,
            db_user.password
        ):
            raise ValueError("Invalid email or password.")

        token = create_access_token(
            {
                "sub": db_user.username,
                "email": db_user.email,
                "role": db_user.role
            }
        )

        return token