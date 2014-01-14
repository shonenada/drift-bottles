#-*- coding: utf-8-
from flask import Blueprint, render_template
from flask import request, redirect, url_for, jsonify
from flask.ext.login import login_required, current_user

from drift.app import rbac, db
from drift.bottle.model import Bottle
from drift.bottle.form import ThrowForm


bottle_app = Blueprint('bottle', __name__)


@bottle_app.route('/bottles')
@login_required
def leadin():
    throw_form = ThrowForm()
    return render_template('bottle/leadin.html', throw_form=throw_form)


@bottle_app.route('/river')
@login_required
def river():
    page = int(request.args.get('page', 1))
    bottles = Bottle.query.filter_by(state='normal').paginate(
        page = page,
        per_page = 20
    )
    return render_template('bottle/bottles.html', bottles=bottles)


@bottle_app.route('/throw', methods=['POST'])
@login_required
def throw():
    form = ThrowForm()
    if form.validate_on_submit():
        paper = form.data['paper']
        bottle = Bottle(paper, current_user)
        db.session.add(bottle)
        db.session.commit()
        return jsonify(success=True, message=u'成功扔出一支瓶子', categore='notice')
    if form.errors:
        return jsonify(success=False, messages=form.errors.values())

@bottle_app.route('/pick', methods=['POST'])
@login_required
def pick():
    return None
