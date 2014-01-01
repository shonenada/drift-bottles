from uuid import uuid4
from hashlib import sha256
from datetime import datetime

from flask.ext.sqlalchemy import BaseQuery
from flask_rbac import RBACRoleMixinModel, RBACUserMixinModel

from drift.app import db
from drift.bottle.model import Bottle


roles_parents = db.Table(
    'roles_parents',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
    db.Column('parent_id', db.Integer, db.ForeignKey('role.id'))
)

users_roles = db.Table(
    'users_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)


class UserQuery(BaseQuery):

    def authenticate(self, email, raw_passwd):
        user = self.filter(User.email == email).first()
        if user and user.check_password(raw_passwd):
            return user
        return None


class Role(db.Model, RBACRoleMixinModel):

    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    parents = db.relationship('Role', secondary=roles_parents,
                              primaryjoin=(id == roles_parents.c.role_id),
                              secondaryjoin=(id == roles_parents.c.parent_id),
                              backref=db.backref('children', lazy='dynamic'))
    users = db.relationship('User', secondary=users_roles,
                            backref=db.backref('roles', lazy='dynamic'))

    def __init__(self, name):
        self.name = name

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return "<Role: %s>" % self.name

    @staticmethod
    def get_by_name(name):
        return self.query.filter_by(name=name).first()


class User(db.Model, RBACUserMixinModel):

    query_class = UserQuery
    USER_STATE = ('normal', 'unactivate', 'deleted')

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(32))
    email = db.Column(db.String(50))
    nickname = db.Column(db.String(20))
    is_male = db.Column(db.Boolean, default=True)
    join_time = db.Column(db.DateTime, default=datetime.utcnow())
    salt = db.Column(db.String(32), nullable=False)
    state = db.Column(db.Enum(name='user_state', *USER_STATE))
    bottles = db.relationship(
        'Bottle', uselist=True,
        backref=db.backref('user', uselist=False)
    )

    def __init__(self, email, raw_pw, nickname, is_male=True):
        self.email = email
        self.change_password(raw_pw)
        self.nickname = nickname
        self.is_male = is_male
        self.state = 'normal'

    def get_id(self):
        return self.id

    def change_password(self, raw_passwd):
        self.salt = uuid4().hex
        self.password = self._hash_password(self.salt, raw_passwd)

    def check_password(self, raw_passwd):
        _hashed_password = self._hash_password(self.salt, raw_passwd)
        return (self.password == _hashed_password)

    def is_active(self):
        return (self.state == 'normal')

    def is_anonymous(self):
        return (self.email is None)

    def is_authenticated(self):
        return (self.state == 'normal')

    @staticmethod
    def _hash_password(salt, password):
        hashed = sha256()
        hashed.update("<%s|%s>" % (salt, password))
        return hashed.hexdigest()
