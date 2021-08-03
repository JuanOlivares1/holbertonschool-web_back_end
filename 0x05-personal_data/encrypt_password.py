#!/usr/bin/env python3
""" Module - personal data, encryption """
import bcrypt


def hash_password(password: str) -> bytes:
    """ encrypts password
    """
    psswrd = bytes(password, 'utf-8')
    hashed = bcrypt.hashpw(psswrd, bcrypt.gensalt())
    return hashed
