from enum import unique
from . import db
from flask_login import UserMixin


class Person(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(20))
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
