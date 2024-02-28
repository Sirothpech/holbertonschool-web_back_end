#!/usr/bin/env python3
"""T5
"""

import uuid
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hash password
    """
    bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(bytes, salt)

    return hash


def _generate_uuid(self) -> str:
    """Generate a new UUID
    """
    new_uuid = uuid.uuid4()
    return str(new_uuid)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a user with a given email and password
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Validates login credentials
        """
        try:
            user = self._db.find_user_by(email=email)
            entered_password = password.encode('utf-8')

            return bcrypt.checkpw(entered_password, user.hashed_password)
        except NoResultFound:
            return False
