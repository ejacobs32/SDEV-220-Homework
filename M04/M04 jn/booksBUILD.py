from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///books.db', echo=True)
base = declarative_base()

class Books (base):

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)

    def __init__(self, id, title, author, year):
        self.id=id
        self.title=title
        self.author=author
        self.year=year

base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

items = [
    [2, "At Midnight", "Rosy Hawks", 2012],
    [3, "Goofy Joke", "Nimble Smith", 1356],
    [4, "Rank 3 Overdrive", "H P Goober", 1978],
    [5, "I Just Prefer Writing SQL", "Linsy E Icecream", 2031],
    [6, "Ey Dount Nough Hou Tue Ceppell", "Myspeslled A Namme", 2020],
]

for item in items:
    book = Books(item[0], item[1], item[2], item[3])
    session.add(book)

session.commit()