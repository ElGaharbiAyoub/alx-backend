#!/usr/bin/env python3
""" Basic Babel setup """
from flask_babel import Babel
from typing import Union, Dict, List
import pytz
from flask import Flask, render_template, request, g


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Union[Dict, None]:
    """Retrieves a user based on a user id"""
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request() -> None:
    """
    Add user to flask.g if user is found
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """use a user’s preferred local if it is supported."""
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    if g.user:
        loc = g.user.get('locale')
        if loc in app.config['LANGUAGES']:
            return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """use a user’s preferred timezone if it is supported."""
    tz = request.args.get('timezone')
    if tz:
        try:
            pytz.timezone(tz)
            return tz
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        tz = g.user.get('timezone')
        if tz:
            try:
                pytz.timezone(tz)
                return tz
            except pytz.exceptions.UnknownTimeZoneError:
                pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', strict_slashes=False)
def index() -> str:
    """ Returns the index page """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
