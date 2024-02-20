#!/usr/bin/env python3
"""
Encrypt passwords
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password.

    """
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check if a password matches its hashed version.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The plain text password to check.

    Returns:
        bool: True if the password is valid, False otherwise.

    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
