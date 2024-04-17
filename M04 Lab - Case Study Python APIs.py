from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # Use your own URI
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

@app.route('/books', methods=['POST'])
def create_book():
    new_book_data = request.get_json()
    new_book = Book(**new_book_data)
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book_data), 201

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.serialize for book in books]), 200

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book.serialize), 200

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    updated_book_data = request.get_json()
    book = Book.query.get(id)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    book.update(updated_book_data)
    db.session.commit()
    return jsonify(book.serialize), 200

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({'result': 'Book deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
