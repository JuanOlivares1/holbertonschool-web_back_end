#!/usr/bin/env python3
""" Auth module
"""
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import Union


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

    def create_session(self, email: str) -> [str, None]:
        """ generates sessions
        """
        try:
            user = self._db.find_user_by(email=email)
            sess_id = _generate_uuid()
            self._db.update_user(user.id, session_id=sess_id)
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> [User, None]:
        """ retrieve user by session id
        """
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ destroy a session"""
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            pass


def _hash_password(password: str) -> bytes:
    """ hashes a password with bcrypt
    """
    passwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passwd, salt)
    return hashed


def _generate_uuid() -> str:
    """Generates a unique id"""
    id = uuid.uuid4()
    return str(id)
