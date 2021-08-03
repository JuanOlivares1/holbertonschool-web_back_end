#!/usr/bin/env python3
""" Module - personal data """
import re


def filter_datum(fields: str, redaction: str, 
                 message: str, separator: str) -> str:
    """ Regex on string """
    s = messageñ
    for field in fields:
        s = re.sub("(?<={}=)[\w/]*(?=;)".format(field), redaction, s)
    return s
