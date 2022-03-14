from app.database import db, Model
from app.user.models import User
from sqlalchemy.orm import relationship

class Post(Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.UnicodeText)
    author = db.relationship("User", backref=db.backref('Post', order_by=id))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
