from app import db


class User(db.Model):
    __tablename__ = 'experience'
    id = db.Column(db.Integer, primary_key=True)
    pid=db.Column(db.Integer, db.ForeignKey('docBasicInfo.id'))
    hospitalName = db.Column(db.String(80), default=None)
    start= db.Column(db.String(80), default=None)
    end = db.Column(db.String(80), default=None)
    designation = db.Column(db.String(80), default=None)




