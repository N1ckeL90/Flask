from sqlalchemy import Column, Integer, String, Text, ForeignKey

from blog.models.database import db


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(80), unique=True)
    text = Column(Text)
    author = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return f'<Article # {self.id} {self.title}>'
