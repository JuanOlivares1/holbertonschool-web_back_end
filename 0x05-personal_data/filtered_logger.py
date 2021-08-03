#!/usr/bin/env python3
""" Module - personal data """
import re
from typing import List
import logging
from datetime import datetime


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """ filter values in incoming log records using filter_datum
        """
        msg = filter_datum(self.fields, self.REDACTION,
                           record.msg, self.SEPARATOR).replace(";", "; ")
        rtn = self.FORMAT
        rtn = rtn.replace("%(name)s", record.name)
        rtn = rtn.replace("%(levelname)s", record.levelname)
        rtn = rtn.replace("%(asctime)-15s",
                          datetime.fromtimestamp(record.created - 15)
                                  .strftime('%Y-%m-%d %H:%M:%S,%f'))
        return rtn.replace("%(message)s", msg)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Filter data with regex and obfuscate """
    msg = message
    for field in fields:
        msg = re.sub(r"(?<={}=)[^{}]*(?={})".format(field, separator,
                                                    separator),
                     redaction, msg)
    return msg
