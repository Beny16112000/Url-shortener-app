from . import db
from flask_login import UserMixin


# Database


class User(UserMixin ,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(1000),nullable=False)
    last_name = db.Column(db.String(1000),nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100),nullable=False)



class UrlShortener(db.Model):
    __tablename__ = 'urlshortener'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    url = db.Column(db.String(1000),nullable=False)
    shorter = db.Column(db.String(1000),nullable=False, unique=True)
    click = db.Column(db.Integer,nullable=False)


class UrlShortenerModel(db.Model):
    __tablename__ = 'urlshortenermodel'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    url = db.Column(db.String(1000),nullable=False)
    shorter = db.Column(db.String(1000),nullable=False, unique=True)
    click = db.Column(db.Integer, nullable=False)


