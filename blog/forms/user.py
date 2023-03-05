from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserBaseForm(FlaskForm):
    first_name = StringField('Имя')
    last_name = StringField('Фамилия')
    username = StringField(
        'Логин',
        [validators.DataRequired()],
    )
    email = StringField(
        'Электронная почта',
        [
            validators.DataRequired(),
            validators.Email(),
            validators.Length(min=6, max=200),
        ],
        filters=[lambda data: data and data.lower()],
    )


class RegistrationForm(UserBaseForm):
    password = PasswordField(
        'Пароль',
        [
            validators.DataRequired(),
            validators.EqualTo('confirm', message='Пароль должен совпадать'),
        ],
    )
    confirm = PasswordField('Повторите пароль')
    submit = SubmitField('Регистрация')


class LoginForm(FlaskForm):
    username = StringField(
        'Логин',
        [validators.DataRequired()],
    )
    password = PasswordField(
        'Пароль',
        [validators.DataRequired()]
    )
    submit = SubmitField('Войти')
