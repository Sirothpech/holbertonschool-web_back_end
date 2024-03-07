#!/usr/bin/env python3
"""Route API
"""
from flask import Flask, g, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Get locale
    """
    lang = app.config['LANGUAGES']

    if 'locale' in request.args and request.args['locale'] in lang:
        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    """Get user
    """
    user_id = int(request.args['login_as'])
    try:
        if user_id in users.keys:
            return users[user_id]
    except Exception:
        return None

@app.before_request
def before_request():
    """Before request
    """
    user = get_user()
    if user:
        g.user = user


@app.route('/')
def index():
    """index.html
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
