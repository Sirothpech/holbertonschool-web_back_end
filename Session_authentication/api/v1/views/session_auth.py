#!/usr/bin/env python3
"""
Session authentication view for handling login requests.
"""
from flask import Flask, jsonify, request, make_response
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth_login() -> str:
    """
    Handles login requests for Session authentication.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    user_list = User.search({'email': email})

    if not user_list:
        return jsonify({"error": "no user found for this email"}), 404

    user = user_list[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    user_json = user.to_json()

    response = jsonify(user_json)
    response.set_cookie(auth.session_cookie_name, session_id)

    return response
