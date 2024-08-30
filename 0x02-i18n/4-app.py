#!/usr/bin/env python3
""" simple flask app """
from flask_babel import Babel
from flask import Flask, render_template, request
from flask_babel import gettext as _


class Config():
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
# add config class attr to the app config instance
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """gets the language
    current user """
    if 'locale' in request.args:
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def hello_word():
    """ show hello to the world"""
    home_title = "Welcome to Holberton"
    home_header = "Hello world!"
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
