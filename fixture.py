from drift.app import db
from drift.account.model import Role


def _init_roles():
    global roles
    roles = (
        Role('everyone'), Role('local_user')
    )
    roles[1].parents.append(roles[0])
    for role in roles:
        db.session.add(role)


def init_db():
    _init_roles()
    db.session.commit()
