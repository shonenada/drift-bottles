import time
import random

from drift.utils import friendly_time


_filters = {
    'friendly_time': friendly_time,
}

_functions = {
    'random': lambda lower, upper, to_string=True: str(random.randint(lower, upper)) if to_string else random.randint(lower, upper),
}


def setup_filter(app):
    for _fname, _ffunc in _filters.iteritems():
        app.add_template_filter(_ffunc, _fname)


def setup_function(app):
    for _fname, _ffunc in _functions.iteritems():
        app.jinja_env.globals[_fname] = _ffunc
