from sqlalchemy import Column, Integer, String, Boolean, LargeBinary
from flask_login import UserMixin

from blog.models.database import db
from blog.security import flask_bcrypt


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(120), unique=True, nullable=False)
    email = Column(String(255), unique=True, default='', server_default='')
    is_staff = Column(Boolean, nullable=False, default=False)
    article = db.relationship('Article', backref='user', uselist=False)
    first_name = Column(String(120), default='', server_default='')
    last_name = Column(String(120), default='', server_default='')
    _password = Column(LargeBinary, nullable=True)

    def __repr__(self):
        return f'<User # {self.id} {self.username}>'

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return flask_bcrypt.check_password_hash(self._password, password)
