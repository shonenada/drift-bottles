from flask import Flask

from drift.extension import db
from drift.extension import login_manager
from drift.extension import rbac, setup_rbac
from drift.jinja import setup_filter, setup_function
from drift.master.view import master_app
from drift.account.view import account_app
from drift.bottle.view import bottle_app
from drift.account.service import load_user


def create_app(import_name=None, config=None):
    app = Flask(import_name or __name__)

    app.config.from_object('drift.settings')

    if config:
        app.config.from_pyfile(config)

    db.init_app(app)

    login_manager.init_app(app)

    # rbac.init_app(app)
    # setup_rbac(app)

    setup_filter(app)
    setup_function(app)

    app.register_blueprint(master_app)
    app.register_blueprint(account_app)
    app.register_blueprint(bottle_app)

    return app
