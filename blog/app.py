from flask import Flask, render_template
from blog.user.views import user
from blog.article.views import article
from blog.models.database import db
from blog.views.auth import auth_app, login_manager


app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(article)
app.register_blueprint(auth_app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "_&xgpaf_@-(6c#_n6eqb9(it947^!7x1c5lylhru9yrixyn2h!"

db.init_app(app)
login_manager.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    from blog.models import User
    admin = User(username='admin', is_staff=True)
    user1 = User(username='Павел')
    user2 = User(username='Сергей')
    user3 = User(username='Ольга')
    user4 = User(username='Екатерина')

    db.session.add(admin)
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.commit()

    print('Done!')


@app.cli.command('create-articles')
def create_articles():
    from blog.models.article import Article
    article1 = Article(title='Статья 1', text='Описание статьи 1', author=2)
    article2 = Article(title='Статья 2', text='Описание статьи 2', author=3)
    article3 = Article(title='Статья 3', text='Описание статьи 3', author=4)
    article4 = Article(title='Статья 4', text='Описание статьи 4', author=2)

    db.session.add(article1)
    db.session.add(article2)
    db.session.add(article3)
    db.session.add(article4)
    db.session.commit()

    print('Done!')
