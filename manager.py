from flask.ext.script import Manager, Server

from drfitbottles.app import create_app


application = create_app()
server = Server()
manager = Manager(application)
manager.add_command("runserver", server)


if __name__ == '__main__':
    manager.run()
