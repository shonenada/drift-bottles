from uuid import uuid4
from hashlib import sha256
from datetime import datetime

from drift.app import db


class User(db.Model):

    USER_STATE = ('normal', 'unactivate', 'deleted')

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(32))
    nickname = db.Column(db.String(20))
    is_male = db.Column(db.Boolean, default=True)
    join_time = db.Column(db.DateTime, default=datetime.utcnow())
    salt = db.Column(db.String(32), nullable=False)
    state = db.Column(db.Enum(name='user_state', *USER_STATE))
    bottles = db.relationship(
        'Bottle', lazy='dynamic',
        backref=db.backref('user', uselist=False, lazy='dynamic')
    )

    def __init__(self, email, raw_pw, is_male=True):
        self.email = email
        self.password = change_password(raw_pw)
        self.is_male = is_male
        self.state = 'normal'

    def change_password(self, raw_passwd):
        self.salt = uuid4().hex
        self.hashed_password = self._hash_password(self.salt, raw_passwd)

    def check_password(self, raw_passwd):
        _hashed_password = self._hash_password(self.salt, raw_passwd)
        return (self.hashed_password == _hashed_password)

    def is_active(self):
        return (self.state == 'normal')

    def is_anonymous(self):
        return (self.email is None)

    @staticmethod
    def _hash_password(salt, password):
        hashed = sha256()
        hashed.update("<%s|%s>" % (salt, password))
        return hashed.hexdigest()
