#!/usr/bin/env python3
""" simple flask app """
from flask_babel import Babel
from flask import Flask, render_template, request


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
    """gets the langueage
    current user """
    return request.accept_languages.best_match(
        app.config['LANGUAGES']
        )


@app.route('/')
def hello_word():
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
