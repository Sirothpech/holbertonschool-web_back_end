#!/usr/bin/env python3
""" Empty session
"""
import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    SessionAuth Class

    This class inherits from the Auth class and is intended for creating a new
    authentication mechanism based on sessions.

    Methods:
        (No additional methods for now)

    Attributes:
        (No additional attributes for now)
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        if user_id is None or type(user_id) is not str:
            return None

        # Generate a Session ID using uuid4()
        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id
