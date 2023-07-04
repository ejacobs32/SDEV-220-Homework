from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80))
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.book_name}, by {self.author}. Published by {self.publisher}"





@app.route('/')
def index():
    return "Hi..."


@app.route('/books')
def get_books():

    with app.app_context():
        books = Book.query.all()

    output = []
    for book in books:
        book_data = {'book_name':book.book_name,
                     'author':book.author,
                     'publisher':book.publisher,}
        output.append(book_data)
    return output


@app.route('/books/<id>')
def get_book(id):
    with app.app_context():
        book = Book.query.get_or_404(id)
    return {'book_name':book.book_name,
'author':book.author,
'publisher':book.publisher,}


@app.route('/books', methods=['POST'])
def add_book():
    with app.app_context():
        book = Book(name=request.json['book_name'],
author=request.json['author'],
publisher=request.json['publisher'],)
        db.session.add(book)
        db.session.commit()
        return {'id': book.id}


@app.route('/books/<id>', methods=['DELETE'])
def delete_book():
    with app.app_context():
        book = Book.query.get(id)
        if book is None: return {"error":"not found"}
        db.session.delete(book)
        db.session.commit()
    return {"message": "Book Burned"}



#with app.app_context():
    
    #db.create_all()
    #book = Book(book_name="Book 1", author="Author 1", publisher="Publisher 1")
    #db.session.add(book)
    #book = Book(book_name="Book 2", author="Author 2", publisher="Publisher 2")
    #db.session.add(book)
    #book = Book(book_name="Book 3", author="Author 3", publisher="Publisher 3")
    #db.session.add(book)
    #book = Book(book_name="Book 4", author="Author 4", publisher="Publisher 4")
    #db.session.add(book)
    #db.session.commit()
    #print(Book.query.all())