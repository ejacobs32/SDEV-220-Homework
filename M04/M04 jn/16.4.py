import sqlite3
conn = sqlite3.connect('books.db')
curs = conn.cursor()
try:
    curs.execute(
        '''CREATE TABLE books
        (id INT PRIMARY KEY,
        title VARCHAR(20),
        author VARCHAR(20),
        year INT)'''
        )
except:
    pass

curs.execute('INSERT INTO books VALUES(1, "Cars and Mud", "Lilly Atwood", 1997)')
curs.execute('INSERT INTO books VALUES(2, "We All Lyft Together", "Spazz", 2023)')
curs.execute('INSERT INTO books VALUES(3, "I\'m Stuck in the Past, HELP!", "Chris Pratt Cellphone", 1403)')
curs.execute('INSERT INTO books VALUES(4, "Three Sticks", "Unknown", 1313)')

curs.execute('SELECT * FROM books')
books = curs.fetchall()
print(books)