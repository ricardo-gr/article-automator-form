from flask import Blueprint, jsonify, request, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Article, User, ArticleStatus
from .database import db

bp = Blueprint('main', __name__)

@bp.route('/')
@login_required
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles, ArticleStatus=ArticleStatus)

@bp.route('/api/articles', methods=['GET'])
@login_required
def get_articles():
    articles = Article.query.all()
    return jsonify([{
        'id': article.id,
        'title': article.title,
        'url': article.url,
        'status': article.status.value,
        'timestamp': article.timestamp.isoformat(),
        'user': {
            'id': article.user.id,
            'name': article.user.name,
            'email': article.user.email
        }
    } for article in articles])

@bp.route('/api/articles', methods=['POST'])
@login_required
def create_article():
    data = request.get_json()
    
    article = Article(
        title=data['title'],
        url=data['url'],
        user=current_user,
        status=ArticleStatus.PENDING
    )
    db.session.add(article)
    db.session.commit()
    
    return jsonify({
        'id': article.id,
        'title': article.title,
        'url': article.url,
        'status': article.status.value,
        'user': {
            'id': current_user.id,
            'email': current_user.email
        }
    }), 201

@bp.route('/api/articles/<int:article_id>/cancel', methods=['POST'])
@login_required
def cancel_article(article_id):
    article = Article.query.get_or_404(article_id)
    article.status = ArticleStatus.CANCELLED
    db.session.commit()
    return jsonify({'message': 'Article cancelled successfully',
                    'status': 'success'}) 