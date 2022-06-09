from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phoneNo = db.Column(db.String(11) , nullable=False)
    password = db.Column(db.String(120), nullable=False)
    isProfileCompleted=db.Column(db.Boolean,nullable=False)
    role = db.Column(db.String(120),nullable=False)
