#-*- coding: utf-8
from flask import Blueprint, render_template
from flask import request, redirect, url_for, jsonify
from flask.ext.login import login_required
from flask.ext.login import login_user, logout_user, current_user

from drift.app import db
from drift.utils import flash
from drift.account.form import SignInForm, SignUpForm
from drift.account.model import User, Role


account_app = Blueprint('account', __name__, template_folder='../templates')


@account_app.route('/signin', methods=['POST'])
def signin():
    if not current_user.is_anonymous():
        return jsonify(success=True)
    form = SignInForm()
    if form.validate_on_submit():
        email = form.data['email'].strip()
        raw_passwd = form.data['password'].strip()
        is_remember_me = form.data.get('loginkeeping', 'off') == 'on'
        user = User.query.authenticate(email, raw_passwd)
        if user:
            login_user(user, force=True, remember=is_remember_me)
            flash(message=u'登录成功', category='notice')
            return jsonify(success=True)
        else:
            return jsonify(message=u'帐号或密码错误', category='warn')
    if form.errors:
        return jsonify(success=False, message=form.errors.values(), category='warn')


@account_app.route('/signup', methods=['POST'])
def signup():
    if not current_user.is_anonymous():
        return jsonify(success=True)
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.data['email'].strip()
        nickname = form.data['nickname'].strip()
        db_user = User.query.filter_by(email=email).count()
        if db_user > 0:
            return jsonify(success=False, message=u'该邮箱已注册', category='warn')
        db_user = User.query.filter_by(nickname=nickname).count()
        if db_user > 0:
            return jsonify(success=False, message=u'该昵称已被使用', category='warn')
        raw_passwd = form.data['password'].strip()
        user = User(email, raw_passwd, nickname)
        local_user = Role.query.filter_by(name='local_user').first()
        user.roles.append(local_user)
        db.session.add(user)
        db.session.commit()
        flash(message=u'注册成功', category='notice')
        return jsonify(success=True)
    if form.errors:
        return jsonify(success=False, messages=form.errors.values(), category='warn')


@account_app.route('/signout')
@login_required
def signout():
    logout_user()
    flash(u'退出成功', 'notice')
    return redirect(url_for('master.index'))


@account_app.route('/account')
@login_required
def account():
    return 'test'