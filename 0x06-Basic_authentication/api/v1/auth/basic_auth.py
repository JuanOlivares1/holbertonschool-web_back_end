#!/usr/bin/env python3
""" Module of API Basic Authentication
"""
from .auth import Auth
from models.user import User


class BasicAuth(Auth):
    """ Basic Auth class
    """
    def current_user(self, request=None) -> TypeVar('User'):
        """Current user and basic authentication"""
        a_header = self.authorization_header(request)
        m_base64 = self.extract_base64_authorization_header(a_header)
        n_base64 = self.decode_base64_authorization_header(m_base64)
        user, password = self.extract_user_credentials(n_base64)
        obj = self.user_object_from_credentials(user, password)

        return obj
