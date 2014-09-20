# coding: utf-8
import datetime
from ._base import db


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    avatar = db.Column(db.String(200))
    birth_year = db.Column(db.String(20))
    death_year = db.Column(db.String(20))
    desc = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    dynasty_id = db.Column(db.Integer, db.ForeignKey('dynasty.id'))
    dynasty = db.relationship('Dynasty',
                              backref=db.backref('artists',
                                                 lazy='dynamic',
                                                 order_by="asc(Artist.birth_year)"))

    def __repr__(self):
        return '<Artist %s>' % self.name


class Dynasty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    abbr = db.Column(db.String(50), unique=True)
    desc = db.Column(db.Text())
    start_year = db.Column(db.Integer)
    end_year = db.Column(db.Integer)

    def __repr__(self):
        return '<Dynasty %s>' % self.name