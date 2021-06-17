#DELETE Method
from flask import Flask, request

app = Flask(__name__)

books = [
    {"title" : "book1", "price" : 199, "id" : 1, "author" : "admin"}
]

@app.route("/")
def hello():
    q = request.args.get('q')
    print(q)
    return {"message" : "Hello"}, 201
    
@app.route('/book', methods=['POST','GET', 'PUT', 'DELETE'])
def book():
    if request.method == 'POST':
        body = request.get_json()
        books.append(body)
        return {"message": "Book already add to database","body": body}, 201
    elif request.method == 'GET':
        return {"books" : books}, 200
    elif request.method == 'PUT':
        body = request.get_json()
        for i, book in enumerate(books):
            if book['id'] == body['id']:
                book[i] = body
        return {"message" : "Book has been replace", "body" : body}, 200
    elif request.method == 'DELETE':
        deleteId = request.args.get('id')
        for i, book in enumerate(books) :
            if book['id'] == int(deleteId):
                books.pop(i)
        return {"message" : "Book is deleted"}, 200





if __name__ == '__main__':
    app.run(debug=True)