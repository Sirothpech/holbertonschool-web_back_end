#!/usr/bin/env python3
""" Empty session
"""
import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    Class to manage session-based authentication.

    Inherits from the Auth class.

    Attributes:
        user_id_by_session_id (dict): A dictionary to store the
        mapping of session IDs to user IDs.

    Methods:
        create_session(user_id: str = None) -> str:
            Creates a session ID for a user and stores the mapping
            in the user_id_by_session_id dictionary.

            Args:
                user_id (str): The ID of the user. Defaults to None.

            Returns:
                str: The generated session ID.

    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        if user_id is None or type(user_id) is not str:
            return None

        # Generate a Session ID using uuid4()
        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id
