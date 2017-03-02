# -*- coding: utf-8 -*-
"""User forms."""
from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length

from .models import Card


class CardForm(Form):
    """Card form."""

    artist = StringField('Artist',
                           validators=[Length(min=0, max=50)])
    name = StringField('Name',
                        validators=[DataRequired(), Length(min=2, max=100)])
    year = StringField('Year')
    medium = StringField('Medium')
    notes = TextAreaField('Notes')
    img = StringField('Image', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(CardForm, self).__init__(*args, **kwargs)
        self.card = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(CardForm, self).validate()
        if not initial_validation:
            return False
        return True
