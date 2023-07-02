from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)

engine = create_engine('sqlite:///books.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

books = session.query(Book.title).order_by(Book.title).all()

for title in books:
    print(f"Title: {title[0]}")

session.close()
