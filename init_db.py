from app import create_app
from app.models import User, Article, ArticleStatus
from app.database import db

def init_db():
    app = create_app()
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Check if admin user exists
        admin = User.query.filter_by(email='ricardo@ricardogarciarivera.com').first()
        if not admin:
            admin = User(
                email='ricardo@ricardogarciarivera.com',
                name='Ricardo García',
                is_admin=True
            )
            admin.set_password('admin123')
            
            db.session.add(admin)
            db.session.commit()
            print("Created admin user")
        
        db.session.commit()
        print("Database initialized successfully!")

if __name__ == '__main__':
    init_db() 