#!/usr/bin/env python3
"""T4: password
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash password
    """
    bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(bytes, salt)

    return hash
