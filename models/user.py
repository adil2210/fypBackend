import datetime
from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    total_points = db.Column(db.Float, default=0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow(), onupdate=datetime.datetime.utcnow())
