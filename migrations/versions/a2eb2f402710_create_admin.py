"""Create Admin

Revision ID: a2eb2f402710
Revises: 7588fdab91c6
Create Date: 2023-03-04 09:50:37.152019

"""
from alembic import op
from sqlalchemy.sql import table, column
from sqlalchemy import String, Boolean
from blog.models.user import User
from blog.models.database import db

# revision identifiers, used by Alembic.
revision = 'a2eb2f402710'
down_revision = '7588fdab91c6'
branch_labels = None
depends_on = None


def upgrade():
    user_table = table('user',
                       column('username', String),
                       column('email', String),
                       column('is_staff', Boolean)
                       )
    op.bulk_insert(user_table,
                   [
                       {'username': 'admin', 'email': 'admin@admin.com', 'is_staff': True}
                   ]
                   )


def downgrade():
    user = User.query.filter_by(username='admin').one_or_none()
    db.session.delete(user)
    db.session.commit()
