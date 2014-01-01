#-*- coding: utf-8-
from flask import Blueprint, render_template
from flask import request, redirect, url_for, jsonify
from flask.ext.login import current_user

from drift.account.form import SignInForm, SignUpForm


master_app = Blueprint('master', __name__, template_folder='../templates')


@master_app.route('/')
def index():
    if not current_user.is_anonymous():
        return redirect(url_for('bottle.leadin'))
    sign_in_form = SignInForm()
    sign_up_form = SignUpForm()
    return render_template('index.html',
                           sign_in_form=sign_in_form,
                           sign_up_form=sign_up_form)


@master_app.route('/about')
def about():
    pass


@master_app.route('/contact')
def contact():
    pass
