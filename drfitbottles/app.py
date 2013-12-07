from flask import Flask

from drfitbottles.bottles.view import bottle_app


def create_app():
    app = Flask(__name__)

    app.config['DEBUG'] = True
    
    app.register_blueprint(bottle_app)
    
    return app
