import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Postingan(Base):
    
    __tablename__ = 'postingan'
    
    id = sa.Column('id',sa.Integer, primary_key=True, autoincrement=True)
    author = sa.Column('author', sa.String)
    post = sa.Column('post', sa.String)
    created_at = sa.Column('created_at', sa.DateTime, default=sa.func.NOW())