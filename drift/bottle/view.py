#-*- coding: utf-8-
from flask import Blueprint, render_template
from flask import request, redirect, url_for, jsonify, json
from flask.ext.login import login_required, current_user

from drift.app import rbac, db
from drift.bottle.model import Bottle
from drift.bottle.form import ThrowForm


bottle_app = Blueprint('bottle', __name__)


@bottle_app.route('/leadin')
@login_required
def leadin():
    throw_form = ThrowForm()
    return render_template('bottle/leadin.html', throw_form=throw_form)


@bottle_app.route('/river')
@login_required
def river():
    page = int(request.args.get('page', 1))
    bottles = Bottle.query.filter_by(state='floating').paginate(
        page = page,
        per_page = 20
    )
    return render_template('bottle/bottles.html', bottles=bottles)


@bottle_app.route('/river/bottles')
@login_required
def bottles():
    page = int(request.args.get('page', 1))
    bottles = Bottle.query.filter_by(state='floating').paginate(
        page = page,
        per_page = 20
    ).items
    return jsonify(bottles=[bottle.serialization for bottle in bottles])


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


@bottle_app.route('/mine', methods=['GET'])
@login_required
def mine():
    my_bottles = Bottle.query.filter_by(user=current_user).filter(Bottle.state!='deleted').all()
    return jsonify(bottles=[bottle.serialization for bottle in my_bottles])


@bottle_app.route('/pick', methods=['PUT'])
@login_required
def pick():
    bid = request.form.get('bottle_id')
    bottle = Bottle.query.get(bid)
    bottle.state = 'unfloat'
    db.session.add(bottle)
    db.session.commit()
    return jsonify(success=True, message=u'操作成功')


@bottle_app.route('/throw_out', methods=['PUT'])
@login_required
def throw_out():
    bid = request.form.get('bottle_id')
    bottle = Bottle.query.get(bid)
    bottle.state = 'floating'
    db.session.add(bottle)
    db.session.commit()
    return jsonify(success=True, message=u'操作成功')


@bottle_app.route('/trash', methods=['DELETE'])
@login_required
def trash():
    bid = request.form.get('bottle_id')
    bottle = Bottle.query.get(bid)
    bottle.state = 'deleted'
    db.session.add(bottle)
    db.session.commit()
    return jsonify(success=True, message=u'操作成功')
