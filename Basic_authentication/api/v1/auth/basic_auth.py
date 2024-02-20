#!/usr/bin/env python3
""" BasicAuth module
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> TypeVar('User'):
        """ Extracts the Base64 part of the Authorization
        header for Basic Authentication
        """
        if authorization_header is None or \
                not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.replace("Basic ", "", 1)

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ Decodes a Base64 Authorization header
        """
        if base64_authorization_header is None or \
                not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except Exception:
            return None
