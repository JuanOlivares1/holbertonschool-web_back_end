#!/usr/bin/env python3
""" Module session auth
"""
import uuid
from .auth import Auth


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
