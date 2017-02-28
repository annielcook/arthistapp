# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, request, flash
from flask_login import login_required
from arthistapp.card.models import Card
from arthistapp.card.forms import CardForm

blueprint = Blueprint('card', __name__, url_prefix='/cards', static_folder='../static')


@blueprint.route('/')
@login_required
def cards():
    """Show cards"""
    cards = Card.query.all()
    return render_template('cards/all.html', cards=cards)


@blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = CardForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        Card.create(artist=form.artist.data, name=form.name.data, year=form.year.data, medium=form.year.data, img=form.img.data)
        flash('Successfully added!')
    return render_template('cards/add.html', form=form)
