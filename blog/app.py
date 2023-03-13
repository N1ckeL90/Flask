import os

from flask import Flask, render_template
from flask_migrate import Migrate

from blog.views.user import user
from blog.views.article import article
from blog.views.author import author
from blog.models.database import db
from blog.views.auth import auth_app, login_manager
from blog.security import flask_bcrypt
from blog import commands


cfg_name = os.environ.get('CONFIG_NAME') or 'ProductionConfig'

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(article)
app.register_blueprint(author)
app.register_blueprint(auth_app)
app.config.from_object(f'blog.configs.{cfg_name}')

db.init_app(app)
login_manager.init_app(app)
flask_bcrypt.init_app(app)

migrate = Migrate(app, db, compare_type=True)

app.cli.add_command(commands.create_admin)
app.cli.add_command(commands.create_articles)
app.cli.add_command(commands.create_tags)


@app.route('/')
def index():
    return render_template('index.html')
