from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False, index=True)
    author = Column(String(300), index=True)
    language = Column(String(100), index=True)
    year = Column(Integer)
    cover_url = Column(Text)
    source = Column(String(100))
    source_id = Column(String(300), index=True)
    description = Column(Text)
    read_url = Column(Text)
    download_url = Column(Text)
