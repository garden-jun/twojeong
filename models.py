from app import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String(200), nullable=False)
