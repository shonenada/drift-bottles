import os.path

from flask.ext.script import Manager, Server

from drift.app import create_app
from drift.app import db


app_root = os.path.dirname(os.path.realpath(__name__))

application = create_app('drift', os.path.join(app_root, 'development.conf'))
server = Server()
manager = Manager(application)
manager.add_command('runserver', server)


@manager.command
def createdb(config="development.conf"):
    config_file = os.path.join(app_root, config)
    application.config.from_pyfile(config_file)
    with application.test_request_context():
        # import all Models here
        from drift.bottle.model import Bottle
        from drift.account.model import User, Role, roles_parents, users_roles
        db.create_all()
    print 'Created Database!'


@manager.command
def initdb(config="development.conf"):
    config_file = os.path.join(app_root, config)
    application.config.from_pyfile(config_file)
    with application.test_request_context():
        # Initial data for test
        from fixture import init_db
        init_db()
    print "Initialized Database!"


@manager.command
def syncdb(config="development.conf"):
    createdb(config)
    initdb(config)


if __name__ == '__main__':
    manager.run()
