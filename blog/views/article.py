from flask import Blueprint, render_template, redirect, url_for, current_app, request
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog.forms.article import CreateArticleForm
from blog.models import Article, Author, Tag
from blog.models.database import db

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static', )


@article.route('/', endpoint='list')
def article_list():
    articles = Article.query.all()
    return render_template(
        'articles/article_list.html',
        articles=articles)


@article.route('/<int:pk>', endpoint='details')
def get_article(pk: int):
    article = Article.query.filter_by(id=pk).options(joinedload(Article.tags)).one_or_none()
    if article is None:
        raise NotFound(f'Статья с id = {pk} не найдена')
    return render_template(
        'articles/article_detail.html',
        article=article,
    )


@article.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]
    if request.method == "POST" and form.validate_on_submit():
        article = Article(title=form.title.data.strip(), text=form.body.data, author_id=current_user.id)
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                article.tags.append(tag)
        db.session.add(article)
        if current_user.author:
            # use existing author if present
            article.author = current_user.author
        else:
            # otherwise create author record
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author_id = author.id
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("article.details", pk=article.id))
    return render_template("articles/create.html", form=form, error=error)
