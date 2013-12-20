from flask import Blueprint, render_template
from flask import request, redirect, url_for, jsonify


bottle_app = Blueprint('bottle', __name__, template_folder='../templates')


@bottle_app.route('/')
def index():
    return render_template('index.html')


@bottle_app.route('/show')
def show():
    page = int(request.args.get('page', 1))
    return render_template('bottles.html')
