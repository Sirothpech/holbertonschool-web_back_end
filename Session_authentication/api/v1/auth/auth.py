#!/usr/bin/env python3
""" Module to manage the API authentication
"""
import os
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require authentication
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Authorization header
        """
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user
        """
        return None

    def session_cookie(self, request=None) -> str:
        """ Session cookie value from request
        """
        if request is None:
            return None

        # Get the session name from the environment variable
        session_name = os.getenv("SESSION_NAME", "_my_session_id")

        # Return the value of the session cookie
        return request.cookies.get(session_name)
