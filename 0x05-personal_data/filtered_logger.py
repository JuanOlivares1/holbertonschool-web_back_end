#!/usr/bin/env python3
""" Module - personal data """
import re
from typing import List
import logging
import mysql.connector
import os


PII_FIELDS = ("name", "email", "ssn", "password", "phone")


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
                           super().format(record), self.SEPARATOR)
        return msg


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Filter data with regex and obfuscate """
    msg = message
    for field in fields:
        msg = re.sub(r"(?<={}=)[^{}]*(?={})".format(field, separator,
                                                    separator),
                     redaction, msg)
    return msg


def get_logger() -> logging.Logger:
    """ generates a logger """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector:
    """ Get data from db
    """
    auth = {
        'user': os.environ["PERSONAL_DATA_DB_USERNAME"],
        'password': os.environ["PERSONAL_DATA_DB_PASSWORD"],
        'host': os.environ["PERSONAL_DATA_DB_HOST"],
        'database': os.environ["PERSONAL_DATA_DB_NAME"]
    }
    cnx = mysql.connector.connect(auth)
    return cnx
