#!/usr/bin/env python3
""" simple flask app """
from flask-babel import Babel
from flask import Flask, render_template


class Config():
"""config class"""
    LANGUAGES = ["en","fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config) # add config class attr to the app.config instance
babel = Babel(app)

@app.route('/')
def hello_word():
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run
