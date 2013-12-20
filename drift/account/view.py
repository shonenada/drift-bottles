#-*- coding: utf-8
from flask import Blueprint, render_template
from flask import request, redirect, url_for, jsonify
from flask.ext.login import login_user, logout_user, current_user

from drift.app import rbac
from drift.account.form import SignInForm
from drift.account.model import User


account_app = Blueprint('account', __name__, template_folder='../templates')


@account_app.route('/signin', methods=['POST'])
@rbac.allow(['everyone'], ['POST'])
def signin():
    if not current_user.is_anonymous():
        return redirect(url_for('master.index'))
    form = SignInForm()
    if form.validate_on_submit():
        username = request.form['username'].strip()
        raw_passwd = request.form['password'].strip()
        is_remember_me = request.form.get('loginkeeping', 'f') == 'y'
        user = User.query.authenticate(username, raw_passwd)
        if user:
            login_user(user, force=True, remember=is_remember_me)
            return jsonify(messages=u'ok', category='notice')
        else:
            return jsonify(messages=u'帐号或密码错误', category='warn')
    if form.errors:
        return jsonify(messages=form.errors, category='warn', form_errors=True)


@account_app.route('/signup')
def signup():
    pass


@account_app.route('/signout')
def signout():
    pass
