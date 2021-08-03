#!/usr/bin/env python3
""" Module - personal data """
import re


def filter_datum(fields: str, redaction: str,
                 message: str, separator: str) -> str:
    """ Regex on string """
    s = message
    for field in fields:
        s = re.sub(r"(?<={}=)[\w/]*(?=;)".format(field), redaction, s)
    return s
