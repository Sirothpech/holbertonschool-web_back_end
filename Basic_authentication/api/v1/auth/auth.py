#!/usr/bin/env python3
""" Auth module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if authentication is required
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        # Slash tolerant comparison
        if path[-1] != '/':
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path[-1] != '/':
                excluded_path += '/'

            if path.startswith(excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method that returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method that returns None
        """
        return None
