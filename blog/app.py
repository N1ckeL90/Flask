import os

from flask import Flask, render_template
from flask_migrate import Migrate

from blog.user.views import user
from blog.article.views import article
from blog.models.database import db
from blog.views.auth import auth_app, login_manager
from blog.security import flask_bcrypt


cfg_name = os.environ.get('CONFIG_NAME') or 'ProductionConfig'

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(article)
app.register_blueprint(auth_app)
app.config.from_object(f'blog.configs.{cfg_name}')

db.init_app(app)
login_manager.init_app(app)
flask_bcrypt.init_app(app)

migrate = Migrate(app, db, compare_type=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.cli.command("create-admin")
def create_admin():
    from blog.models import User
    admin = User(username='admin', is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or 'adminpass'

    db.session.add(admin)
    db.session.commit()

    print('created admin:', admin)


@app.cli.command('create-articles')
def create_articles():
    from blog.models.article import Article
    article1 = Article(title='Статья 1', text='Описание статьи 1', author=1)

    db.session.add(article1)
    db.session.commit()

    print('Done!')
