from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from blog.models.database import db


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False, default='', server_default='')
    text = Column(Text, nullable=False, default='', server_default='')
    author_id = Column(Integer, ForeignKey('author.id'))
    created_at = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship('Author', back_populates='articles')

    def __repr__(self):
        return f'<Article # {self.id} {self.title}>'
