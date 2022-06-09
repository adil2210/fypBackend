from app import db


class User(db.Model):
    __tablename__ = 'education'
    id = db.Column(db.Integer, primary_key=True)
    pid=db.Column(db.Integer, db.ForeignKey('docBasicInfo.id'))
    degree = db.Column(db.String(80), default=None)
    institute = db.Column(db.String(80), default=None)
    yearOfCompletion = db.Column(db.String(80), default=None)



