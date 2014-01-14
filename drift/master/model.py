import json


class SqlalchemyToJSONMixin(object):

    def _to_json(self, cls, to_json=True):
        d = dict()
        for column in cls.__class__.__table__.columns:
            value = getattr(cls, column.name)
            if value is None:
                d[column.name] = str()
            else:
                d[column.name] = value
        if to_json:
            return json.dumps(d)
        else:
            return d

    @property
    def json(self):
        return self._to_json(self)

    @property
    def serialization(self):
        return self._to_json(self, to_json=False)
