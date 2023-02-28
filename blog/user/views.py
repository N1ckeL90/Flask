from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from blog.models import User

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static', )


@user.route('/')
def user_list():
    users = User.query.all()
    return render_template(
        'users/users_list.html',
        users=users,
    )


@user.route('/<int:pk>')
def get_user(pk: int):
    user = User.query.filter_by(id=pk).one_or_none()
    if user is None:
        raise NotFound(f"Пользователя #{pk} не существует!")
    return render_template(
        'users/details.html',
        user=user,
    )
