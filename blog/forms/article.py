from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators, SelectMultipleField


class CreateArticleForm(FlaskForm):
    title = StringField(
        'Заголовок',
        [validators.DataRequired()],
    )
    body = TextAreaField(
        'Текст статьи',
        [validators.DataRequired()]
    )
    tags = SelectMultipleField('Теги', coerce=int)
    submit = SubmitField('Опубликовать')
