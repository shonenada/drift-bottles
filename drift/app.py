from flask import Flask

from drift.bottles.view import bottle_app
from drift.extension import db


def create_app(import_name=None, config=None):
    app = Flask(import_name or __name__)

    app.config.from_object('drift.settings')

    if config:
        app.config.from_pyfile(config)

    db.init_app(app)

    app.register_blueprint(bottle_app)

    return app
