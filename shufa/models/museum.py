# coding: utf-8
import datetime
from ._base import db


class Museum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(200))
    image = db.Column(db.String(200))
    desc = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return '<Museum %s>' % self.name