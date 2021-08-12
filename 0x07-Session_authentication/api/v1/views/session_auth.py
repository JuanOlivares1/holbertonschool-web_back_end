#!/usr/bin/env python3
""" Module handles all routes for Session authentication
"""
from flask import jsonify, request
from models.user import User
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth() -> str:
    """ POST /auth_session/login
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None:
        return jsonify({"error": "email missing"}), 400
    if password is None:
        return jsonify({"error": "password missing"}), 400

    users = User()
    user = None
    for userr in users.search():
        if userr.__dict__['email'] == email:
            user = userr

    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    from os import getenv

    session = auth.create_session(user.id)
    cookie_name = getenv("SESSION_NAME")

    user = jsonify(user.to_json())
    user.set_cookie(cookie_name, session)
    return user


@app_views.route('/auth_session/login', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ DELETE /auth_session/login
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
        return False
    return jsonify({}), 200