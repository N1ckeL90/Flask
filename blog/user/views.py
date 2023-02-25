from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static', )
USERS = {
    1: 'Павел',
    2: 'Сергей',
    3: 'Ольга',
    4: 'Екатерина'
}


@user.route('/')
def user_list():
    return render_template(
        'users/users_list.html',
        users=USERS,
    )


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user_name = USERS[pk]
    except KeyError:
        raise NotFound(f'Пользователь с id = {pk} не найден')
    return render_template(
        'users/details.html',
        user_name=user_name,
    )
