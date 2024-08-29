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


@babel.timezoneselector
def get_timezone():
   """gets the timezone of user"""
    # 1. Check if a timezone is provided in the URL parameters
    timezone_param = request.args.get('timezone')
    if timezone_param:
        try:
            # Validate the provided timezone
            return pytz.timezone(timezone_param).zone
        except UnknownTimeZoneError:
            pass  # Invalid timezone, fall back to other methods

    # 2. Check if the user has a timezone set
    if g.user:
        user_timezone = g.user.get('timezone')
        if user_timezone:
            try:
                # Validate the user-defined timezone
                return pytz.timezone(user_timezone).zone
            except UnknownTimeZoneError:
                pass  # Invalid timezone, fall back to default

    # 3. Default to UTC
    return 'UTC'

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
