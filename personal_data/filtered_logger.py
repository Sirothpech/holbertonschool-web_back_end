#!/usr/bin/env python3
"""
0. Regex-ing
"""

import re


def filter_datum(fields, redaction, message, separator):
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
    return re.sub(regex, f"\\1={redaction}{separator}", message)
