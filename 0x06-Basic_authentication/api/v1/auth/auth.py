#!/usr/bin/env python3
""" Module of API Authentication
"""
from flask import request


class Auth():
    """ Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determine if auth is needed
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Makes header for request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ User request
        """
        return None
