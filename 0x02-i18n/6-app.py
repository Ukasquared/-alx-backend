#!/usr/bin/env python3
""" simple flask app """
from flask_babel import Babel
from flask import Flask, render_template, request, g
from flask_babel import gettext as _


class Config():
    """config class"""
    LANGUAGES = ["en","fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config) # add config class attr to the app.config instance
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """gets the langueage
    current user """
    if 'locale' in request.args:
       locale = request.args.get('locale')
       if locale in app.config['LANGUAGES']:
           return locale
    elif 'locale' in g.user:
        return g.user.get('locale')
    elif request.accept_languages:
        return request.accept_languages.best_match(
            app.config['LANGUAGES'])
    else:
        return app.config['BABEL_DEFAULT_LOCALE']


def get_user(user_id):
    """get user from
    mocked database """
    return users.get(user_id)
    
@app.before_request
def before_request():
    g.user = None
    login_id = request.args.get('login_as')
    if login_id:
        g.user = get_user(int(login_id))

@app.route('/')
def hello_world():
    username = ""
    if g.user:
        username = g.user.get('name')
    return render_template('5-index.html', username=username)

if __name__ == "__main__":
    app.run()
