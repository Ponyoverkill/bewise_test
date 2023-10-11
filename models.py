from sqlalchemy import MetaData, Column, String, ForeignKey, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base(metadata=MetaData())


class Category(Base):
    __tablename__ = 'categories'

    id = Column(BigInteger, primary_key=True, unique=True)
    title = Column(String)
    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True), nullable=True)


class Question(Base):
    __tablename__ = 'questions'

    id = Column(BigInteger, primary_key=True, unique=True)
    answer = Column(String)
    question = Column(String)
    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True), nullable=True)
    category_id = Column(BigInteger, ForeignKey(Category.id))
