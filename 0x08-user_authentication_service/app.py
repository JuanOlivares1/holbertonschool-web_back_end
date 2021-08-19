#!/usr/bin/env python3
""" Auth module
"""
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def bienvenue() -> str:
    """ GET /
      - Bienvenue message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ POST /users
      - Register users
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify(
            {"email": "{}".format(email), "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /sessions
        - login
    """
    email = request.form.get("email")
    password = request.form.get("password")

    valid = AUTH.valid_login(email, password)
    if valid:
        session_id = AUTH.create_session(email)
        res = jsonify({"email": "{}".format(email), "message": "logged in"})
        res.set_cookie("session_id", session_id)
        return res
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
