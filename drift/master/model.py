import json


class SqlalchemyToJSONMixin(object):

    def _to_json(self, cls):
        d = dict()
        for column in cls.__class__.__table__.columns:
            value = getattr(cls, column.name)
            if value is None:
                d[column.name] = str()
            else:
                d[column.name] = value
        return json.dumps(d)

    @property
    def json(self):
        return self._to_json(self)
