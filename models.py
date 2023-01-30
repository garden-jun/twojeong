from app import db
class USER(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String(200), nullable=False)
