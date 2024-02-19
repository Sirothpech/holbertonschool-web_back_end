#!/usr/bin/env python3
"""
1. Log formatter
"""

import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscate sensitive information in a log message.

    Args:
        fields (list): List of fields to obfuscate.
        redaction (str): String to obfuscate the field.
        message (str): Log line.
        separator (str): Separator character.

    Returns:
        str: Obfuscated log message.
    """
    pattern = "|".join(fields)
    regex = f"({pattern})=(.*?){separator}"
    return re.sub(regex, f"\\1={redaction}{separator} ", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields=()):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        log_message = super().format(record)
        filtered_message = filter_datum(self.fields, self.REDACTION,
                                        log_message, self.SEPARATOR)
        return filtered_message
