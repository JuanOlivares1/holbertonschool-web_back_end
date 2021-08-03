#!/usr/bin/env python3
""" Module - personal data """
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Filter data with regex and obfuscate """
    for field in fields:
        message = re.sub(r"(?<={}=)[^;]*(?=;)".format(field),
                         redaction, message)
    return message
