# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required
from arthistapp.card.models import Card
from arthistapp.card.forms import CardForm
from arthistapp.extensions import db

blueprint = Blueprint('card', __name__, url_prefix='/cards', static_folder='../static')


@blueprint.route('/')
@login_required
def cards():
    """Show cards"""
    cards = Card.query.all()
    for card in cards:
        card.formatted_notes = card.format_notes(card.notes)
    return render_template('cards/all.html', cards=cards)


@blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = CardForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        Card.create(artist=form.artist.data, name=form.name.data, year=form.year.data, medium=form.medium.data, notes=form.notes.data, img=form.img.data)
        flash('Successfully added!')
    return render_template('cards/add.html', form=form)

@blueprint.route('/delete/<int:postId>', methods=['POST'])
@login_required
def delete(postId):
    Card.query.filter_by(id=postId).delete()
    db.session.commit()
    cards = Card.query.all()
    return redirect('/cards')


@blueprint.route('/update/<int:postId>', methods=['POST'])
@login_required
def update(postId):
    card = Card.query.get(postId)
    form = CardForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        card.artist = form.artist.data
        card.name = form.name.data
        card.year = form.year.data
        card.medium = form.medium.data
        card.notes = form.notes.data
        card.img = form.img.data
        db.session.commit()
    form.artist.data = card.artist
    form.name.data = card.name
    form.year.data = card.year
    form.medium.data = card.medium
    form.notes.data = card.notes
    form.img.data = card.img
    return render_template('cards/update.html', form=form)
