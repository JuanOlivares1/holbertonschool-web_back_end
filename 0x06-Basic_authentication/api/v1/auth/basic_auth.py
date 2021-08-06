#!/usr/bin/env python3
""" Module of API Basic Authentication
"""
from .auth import Auth
from base64 import b64decode
import binascii


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

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
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
