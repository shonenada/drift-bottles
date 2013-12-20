from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, current_user
from flask_rbac import RBAC


db = SQLAlchemy()
login_manager = LoginManager()
rbac = RBAC()


def setup_rbac(app):
    from drift.account.model import User, Role
    _rbac = app.extensions['rbac'].rbac
    _rbac.set_role_model(Role)
    _rbac.set_user_model(User)
    _rbac.set_user_loader(lambda *args: current_user)
