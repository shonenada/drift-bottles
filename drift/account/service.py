from drift.app import db
from drift.extension import login_manager
from drift.account.model import User


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
