import os
import click

from blog.models.database import db


@click.command("create-admin")
def create_admin():
    from blog.models import User
    from wsgi import app

    admin = User(username='admin', is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or 'adminpass'
    with app.app_context():
        db.session.add(admin)
        db.session.commit()

    print('created admin:', admin)


@click.command('create-tags')
def create_tags():
    from blog.models import Tag
    from wsgi import app

    with app.app_context():
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
