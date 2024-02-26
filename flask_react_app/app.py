from flask import Flask, jsonify, request
import sqlite3

app= Flask (__name__)
DB_NAME = 'books.db'

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS books (
                   id INTEGER PRIMARY KEY,
                   title TEXT NOT NULL,
                   author TEXT NOT NULL
                   )
                   ''')
    conn.commit()
    conn.close()

create_table()

@app.route('/books', methods=['GET'])
def get_books():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT* FROM books')
    books = cursor.fetchall()
    conn.close()
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data.get ('title')
    author = data.get ('author')

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Book added successfully'})

if __name__ == '__main__':
    app.run(debug=True)

