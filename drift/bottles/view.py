#-*- coding: utf-8 -*-
from flask import Blueprint, render_template


bottle_app = Blueprint('bottles', __name__, template_folder='../templates')


@bottle_app.route('/')
def index():
    return render_template('index.html')


@bottle_app.route('/bottles')
def bottles():
    # 返回 漂流瓶数据
    pass


@bottle_app.route('/show')
def show():
    page = request.args.get('page', 1)
    size = request.args.get('size', 10)
    return render_template('bottles.html')
