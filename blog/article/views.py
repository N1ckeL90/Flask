from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static', )
ARTICLES = {
    1: {
        'title': 'Статья 1',
        'text': 'Описание статьи 1',
        'author': {
            'id': 1,
            'user_name': 'Павел'
        }
    },
    2: {
        'title': 'Статья 2',
        'text': 'Описание статьи 2',
        'author': {
            'id': 2,
            'user_name': 'Сергей'
        }
    },
    3: {
        'title': 'Статья 3',
        'text': 'Описание статьи 3',
        'author': {
            'id': 1,
            'user_name': 'Павел'
        }
    },
    4: {
        'title': 'Статья 4',
        'text': 'Описание статьи 4',
        'author': {
            'id': 4,
            'user_name': 'Екатерина'
        }
    }
}


@article.route('/')
def article_list():
    return render_template(
        'articles/article_list.html',
        article=ARTICLES)


@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        article_detail = ARTICLES[pk]
    except KeyError:
        raise NotFound(f'Статья с id = {pk} не найдена')
    return render_template(
        'articles/article_detail.html',
        article=article_detail,
    )
