#!/usr/bin/env python3
""" Module - personal data """
import re


def filter_datum(fields: str, redaction: str,
                 message: str, separator: str) -> str:
    """ Filter data with regex and obfuscate """
    for field in fields:
        message = re.sub(r"(?<={}=)[\w/,.*-]*(?=;)".format(field),
                         redaction, message)
    return message
