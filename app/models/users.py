from app.extensions import db

# Create the database and the database tables

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'image': self.image,
            'password': self.password
            }
    def __init__(self,username,email,password,image):
        self.username = username
        self.email = email
        self.password = password
        self.image = image
        