from server import db

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def save(self):
        db.session.add(self)
        db.session.commit()