#!/usr/bin/env python3
"""Route API
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


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


@app.route('/')
def index():
    """index.html
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
