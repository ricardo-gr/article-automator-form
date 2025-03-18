from flask import Blueprint, request, render_template, redirect, url_for
from .models import Article, User
from .database import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)

@bp.route('/submit', methods=['POST'])
def submit():
    title = request.form['title']
    url = request.form['url']
    user_email = request.form['user']
    
    # Get or create user
    user = User.query.filter_by(email=user_email).first()
    if not user:
        user = User(email=user_email, name=user_email.split('@')[0])  # Simple name generation
    
    new_article = Article(title=title, url=url, user=user)
    db.session.add(new_article)
    db.session.commit()
    return redirect(url_for('main.index')) 