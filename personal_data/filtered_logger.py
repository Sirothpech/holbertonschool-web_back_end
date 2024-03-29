#!/usr/bin/env python3
"""
4. Read and filter data
"""

import re
from typing import List, Tuple
import logging
import mysql.connector
import os


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
    return re.sub(regex, f"\\1={redaction}{separator}", message)


class RedactingFormatter(logging.Formatter):
    """Custom log formatter for redacting sensitive information.

    Attributes:
        REDACTION (str): String to replace sensitive information.
        FORMAT (str): Log format string.
        SEPARATOR (str): Separator character in the log message.

    Args:
        fields (List[str]): List of fields to redact.

    Methods:
        format(record: LogRecord) -> str:
            Format the log record, redacting sensitive information.

    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str] = ()):
        """Initialize the RedactingFormatter.

        Args:
            fields (List[str]): List of fields to redact.

        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record, redacting sensitive information.

        Args:
            record (LogRecord): The log record to be formatted.

        Returns:
            str: The formatted log message.

        """
        log_message = super().format(record)
        filtered_message = filter_datum(self.fields, self.REDACTION,
                                        log_message, self.SEPARATOR)
        return filtered_message


PII_FIELDS: Tuple[str, str, str, str, str] = ("name", "email",
                                              "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """Create and configure a logger.

    Returns:
        logging.Logger: Configured logger object.

    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to the database.

    Returns:
        mysql.connector.connection.MySQLConnection: Database connection object.

    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database_name = os.getenv("PERSONAL_DATA_DB_NAME")

    connection = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database_name
    )

    return connection


def main():
    """Main function to read and filter data."""
    # Configure the logger with the RedactingFormatter
    logger = get_logger()

    # Connect to the database
    db = get_db()
    cursor = db.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM users;")

    # Log the results
    for row in cursor:
        logger.info(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
