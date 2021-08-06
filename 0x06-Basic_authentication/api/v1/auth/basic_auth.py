#!/usr/bin/env python3
""" Module of API Basic Authentication
"""
from .auth import Auth


class BasicAuth(Auth):
    """ Basic Auth class
    """
    def extract_base64_authorization_header(self, 
                                            authorization_header: str) -> str:
        """ Base64 extract
        """
        if authorization_header is None:
            return None

        if authorization_header is not str:
            return None

        if authorization_header[:5] != 'Basic':
            return None
        
        rtn = authorization_header.split()
        if len(rtn) < 1:
            return None
        
        return rtn[1]
