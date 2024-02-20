#!/usr/bin/env python3
""" Empty session
"""
import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Class to manage session-based authentication.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session ID for a user.
        """
        if user_id is None or type(user_id) is not str:
            return None

        # Generate a Session ID using uuid4()
        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id
