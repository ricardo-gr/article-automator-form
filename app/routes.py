from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from .models import Article, User, ArticleStatus
from .database import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    articles = Article.query.all()
    users = User.query.all()
    return render_template('index.html', articles=articles, users=users, ArticleStatus=ArticleStatus)

@bp.route('/submit', methods=['POST'])
def submit():
    title = request.form['title']
    url = request.form['url']
    user_id = request.form['user_id']
    
    user = User.query.get_or_404(user_id)
    new_article = Article(title=title, url=url, user=user)
    db.session.add(new_article)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/api/articles/<int:article_id>/cancel', methods=['POST'])
def cancel_article(article_id):
    article = Article.query.get_or_404(article_id)
    article.status = ArticleStatus.CANCELLED
    db.session.commit()
    return jsonify({'status': 'success'}) 