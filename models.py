from app import db
class USER(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String(200), nullable=False)


class TeamMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    current_personnel = db.Column(db.Integer)
    target_personnel = db.Column(db.Integer)
    one_line_introduce = db.Column(db.String(1000))
    image = db.Column(db.String(10000))
    detail = db.Column(db.String(10000))
    scrap = db.Column(db.Integer)
    area = db.Column(db.String(100))