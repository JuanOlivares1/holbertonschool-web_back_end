#!/usr/bin/env python3
""" Module session auth
"""
import uuid
from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    """ Class session auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ method create_session
        """
        if user_id is None or type(user_id) != str:
            return None
        id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[id] = user_id
        return id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ method user_id_for_session_id
        """
        if session_id is None or type(session_id) != str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ retrieves current user
        """
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        user = User()
        return user.get(user_id)

    def destroy_session(self, request=None):
        """ close session - logout
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        if not self.user_id_by_session_id.pop(session_id, None):
            return False
        else:
            return True
