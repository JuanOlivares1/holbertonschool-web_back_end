#!/usr/bin/env python3
""" Module - personal data, encryption """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Encrypts password
    """
    psswrd = bytes(password, 'utf-8')
    hashed = bcrypt.hashpw(psswrd, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validate that the provided password matches the hashed password
    """
    psswrd = bytes(password, 'utf-8')
    return bcrypt.checkpw(psswrd, hashed_password)
