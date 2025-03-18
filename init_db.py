from app import create_app
from app.models import User, Article, ArticleStatus
from app.database import db

def init_db():
    app = create_app()
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Create dummy user if it doesn't exist
        dummy_user = User.query.filter_by(email='dev@example.com').first()
        if not dummy_user:
            dummy_user = User(
                email='ricardo@ricardogarciarivera.com',
                name='Ricardo García'
            )
            db.session.add(dummy_user)
            db.session.commit()
            print("Created dummy user")
        
        db.session.commit()
        print("Database initialization completed!")

if __name__ == '__main__':
    init_db() 