#!/usr/bin/env python3
""" Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Method - register user
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError('User {} already exists.'.format(email))
        except NoResultFound:
            h_passwd = _hash_password(password)
            user = self._db.add_user(email, h_passwd)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """ determines if login is correct
        """
        try:
            user = self._db.find_user_by(email=email)
            h_passwd = password.encode('utf-8')
            return bcrypt.checkpw(h_passwd, user.hashed_password)
        except NoResultFound:
            return False


def _hash_password(password: str) -> bytes:
    """ hashes a password with bcrypt
    """
    passwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passwd, salt)
    return hashed
