#!/usr/bin/env python3
""" Auth module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method that returns False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method that returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method that returns None
        """
        return None
