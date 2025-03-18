from datetime import datetime
from enum import Enum
from .database import db

class ArticleStatus(Enum):
    PENDING = 'Pending'
    GENERATED = 'Generated'
    POSTED = 'Posted'

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Enum(ArticleStatus), default=ArticleStatus.PENDING, nullable=False)
    
    # Relationship with User model
    user = db.relationship('User', lazy=True, backref=db.backref('articles', lazy=True))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    @classmethod
    def get_or_create(cls, email, name, picture):
        user = cls.query.filter_by(email=email).first()
        if user:
            return user
        else:
            new_user = cls(email=email, name=name)
            db.session.add(new_user)
            db.session.commit()
            return new_user 