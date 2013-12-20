from flask import Blueprint, render_template
from flask import request, redirect, url_for, jsonify

from drift.app import rbac
from drift.account.form import SignInForm


master_app = Blueprint('master', __name__, template_folder='../templates')


@rbac.allow(['everyone'], ['GET'])
@master_app.route('/')
def index():
    form = SignInForm()
    return render_template('index.html', form=form)


@rbac.allow(['everyone'], ['GET'])
@master_app.route('/about')
def about():
    pass


@rbac.allow(['everyone'], ['GET'])
@master_app.route('/contact')
def contact():
    pass
