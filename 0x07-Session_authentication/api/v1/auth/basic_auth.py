#!/usr/bin/env python3
""" Module of API Basic Authentication
"""
from .auth import Auth
from base64 import b64decode
import binascii
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ Basic Auth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Base64 extract
        """
        if authorization_header is None:
            return None

        if type(authorization_header) is not str:
            return None

        if authorization_header[:5] != 'Basic':
            return None

        rtn = authorization_header.split()
        if len(rtn) <= 1:
            return None

        return rtn[1]

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """ Base64 decode
        """
        if base64_authorization_header is None:
            return None

        if type(base64_authorization_header) is not str:
            return None

        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except binascii.Error:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ Extract user method
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if type(decoded_base64_authorization_header) is not str:
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        decode = decoded_base64_authorization_header.split(':')
        return decode[0], decode[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Method to get a User object"""

        if user_email is None or type(user_email) != str:
            return None

        if user_pwd is None or type(user_pwd) != str:
            return None

        user = User()
        objs = user.search()
        obj = None

        for i in objs:
            if i.__dict__['email'] == user_email:
                obj = i

        if not obj or not obj.is_valid_password(user_pwd):
            return None

        return obj

    def current_user(self, request=None) -> TypeVar('User'):
        """ Basic Auth of current user
        """
        a_header = self.authorization_header(request)
        b64 = self.extract_base64_authorization_header(a_header)
        n_b64 = self.decode_base64_authorization_header(b64)
        user, password = self.extract_user_credentials(n_b64)
        obj = self.user_object_from_credentials(user, password)

        return obj
