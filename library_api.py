from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data storage
books = {}
members = {}
book_id_counter = 1
member_id_counter = 1

# Routes for Books
@app.route('/books', methods=['POST'])
def add_book():
    global book_id_counter
    data = request.json
    book = {
        'id': book_id_counter,
        'title': data.get('title'),
        'author': data.get('author'),
        'available': True
    }
    books[book_id_counter] = book
    book_id_counter += 1
    return jsonify(book), 201

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(list(books.values())), 200

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = books.get(book_id)
    if book:
        return jsonify(book), 200
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    book = books.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    book['title'] = data.get('title', book['title'])
    book['author'] = data.get('author', book['author'])
    book['available'] = data.get('available', book['available'])
    return jsonify(book), 200

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id in books:
        del books[book_id]
        return jsonify({'message': 'Book deleted'}), 200
    return jsonify({'error': 'Book not found'}), 404

# Routes for Members
@app.route('/members', methods=['POST'])
def add_member():
    global member_id_counter
    data = request.json
    member = {
        'id': member_id_counter,
        'name': data.get('name'),
        'email': data.get('email')
    }
    members[member_id_counter] = member
    member_id_counter += 1
    return jsonify(member), 201

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(list(members.values())), 200

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = members.get(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({'error': 'Member not found'}), 404

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.json
    member = members.get(member_id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404

    member['name'] = data.get('name', member['name'])
    member['email'] = data.get('email', member['email'])
    return jsonify(member), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    if member_id in members:
        del members[member_id]
        return jsonify({'message': 'Member deleted'}), 200
    return jsonify({'error': 'Member not found'}), 404

# route for search
@app.route('/books/search', methods=['GET'])
def search_books():
    query_title = request.args.get('title', '').lower()
    query_author = request.args.get('author', '').lower()

    results = []
    for book in books.values():
        if (query_title in book['title'].lower() or not query_title) and \
           (query_author in book['author'].lower() or not query_author):
            results.append(book)

    if results:
        return jsonify(results), 200
    else:
        return jsonify({"message": "No books found matching the criteria"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5500)
