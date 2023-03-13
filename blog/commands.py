import os
import click

from blog.models.database import db


@click.command("create-admin")
def create_admin():
    from blog.models import User
    admin = User(username='admin', is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or 'adminpass'

    db.session.add(admin)
    db.session.commit()

    print('created admin:', admin)


@click.command('create-articles')
def create_articles():
    from blog.models.article import Article
    article1 = Article(title='Статья 1', text='Описание статьи 1', author=1)

    db.session.add(article1)
    db.session.commit()

    print('Done!')


@click.command('create-tags')
def create_tags():
    from blog.models import Tag
    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news"
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print('Tags created')
