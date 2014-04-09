from datetime import datetime

from drift.app import db
from drift.master.model import SqlalchemyToJSONMixin


class Bottle(db.Model, SqlalchemyToJSONMixin):

    BOTTLE_STATE = ('floating', 'unfloat', 'deleted')

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(250))
    created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    state = db.Column(db.Enum('bottle_state', *BOTTLE_STATE))

    def __init__(self, content, user):
        self.user = user
        self.content = content
        self.state = 'floating'
