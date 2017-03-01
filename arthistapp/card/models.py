# -*- coding: utf-8 -*-
"""Card models."""
import datetime as dt


from arthistapp.database import Column, Model, SurrogatePK, db, reference_col, relationship
from arthistapp.extensions import bcrypt


class Card(SurrogatePK, Model):
    """A card in the app."""

    __tablename__ = 'cards'
    artist = Column(db.String(80), nullable=True)
    name = Column(db.String(80),  nullable=False)
    year = Column(db.String(20), nullable=True)
    medium = Column(db.String(30), nullable=True)
    img = Column(db.String(30), nullable=False)
    notes = Column(db.String(500), nullable=True)
    starred = Column(db.Boolean(), default=False)

    def __init__(self, name, img, artist, year, notes, medium, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, img=img, artist=artist, medium=medium, notes=notes, year=year, **kwargs)


    def format_notes(self, notes):
        if notes is None:
            return None
        print notes.split('* ')
        return notes.split('* ')
