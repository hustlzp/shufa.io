# coding: utf-8
import datetime
from ._base import db


class Work(db.Model):
    """作品"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    desc = db.Column(db.Text)
    annotation = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now)

    work_type_id = db.Column(db.Integer, db.ForeignKey('work_type.id'))
    work_type = db.relationship('WorkType', backref=db.backref('works', lazy='dynamic'))

    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    artist = db.relationship('Artist', backref=db.backref('works', lazy='dynamic'))

    museum_id = db.Column(db.Integer, db.ForeignKey('museum.id'))
    museum = db.relationship('Museum', backref=db.backref('works', lazy='dynamic'))

    dynasty_id = db.Column(db.Integer, db.ForeignKey('dynasty.id'))
    dynasty = db.relationship('Dynasty',
                              backref=db.backref('works', lazy='dynamic'))

    def __repr__(self):
        return '<Work %s>' % self.title


class WorkType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __repr__(self):
        return '<WorkType %s>' % self.name


class WorkImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(200))
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    order = db.Column(db.Integer)

    work_id = db.Column(db.Integer, db.ForeignKey('work.id'))
    work = db.relationship('Work', backref=db.backref('images', lazy='dynamic'))

    @property
    def url(self):
        # TODO
        pass

    def __repr__(self):
        return '<WorkImage %s>' % self.filename
