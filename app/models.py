from datetime import datetime
from enum import Enum
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .database import db

class ArticleStatus(Enum):
    PENDING = 'Pending'
    GENERATED = 'Generated'
    POSTED = 'Posted'
    CANCELLED = 'Cancelled'

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Enum(ArticleStatus), default=ArticleStatus.PENDING, nullable=False)
    
    # Relationship with User model
    user = db.relationship('User', lazy=True, backref=db.backref('articles', lazy=True))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def get_or_create(cls, email, name, password):
        user = cls.query.filter_by(email=email).first()
        if user:
            if not user.check_password(password):
                raise ValueError("Invalid password for existing user")
            return user
        else:
            new_user = cls(email=email, name=name)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return new_user 