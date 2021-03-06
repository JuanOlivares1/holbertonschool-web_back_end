#!/usr/bin/env python3
""" Module of API Authentication
"""
from typing import List, TypeVar
from flask import request
from os import getenv


class Auth():
    """ Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determine if auth is needed
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path = path + '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Makes header for request
        """
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ User request
        """
        return None

    def session_cookie(self, request=None):
        """ gets a cookie value from a request
        """
        if request is None:
            return None

        session_name = getenv("SESSION_NAME")
        cookie = request.cookies.get(session_name)
        return cookie
