#!/usr/bin/env python3
"""Seting up basic Flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)


class Config():
    """Config for languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """gets local language
    """
    args = request.args
    if args:
        if 'locale' in args.keys():
            if args['locale'] in app.config['LANGUAGES']:
                return args['locale']

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """gets_user from mocked database
    """
    if request.args:
        if 'login_as' in request.args.keys():
            if int(request.args['login_as']) in users.keys():
                return users[int(request.args['login_as'])]
    return None


@app.before_request
def before_request():
    """before_request
    """
    usr = get_user()
    if usr:
        g.user = usr


@app.route('/')
def index():
    """Route to root page
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
