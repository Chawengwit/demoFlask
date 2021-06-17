#PUT Method
from flask import Flask, request

app = Flask(__name__)

books = [
    {"title" : "book1", "price" : 199, "id" : 1, "author" : "admin"}
]
#PUT (body) {"title" : "book2", "price" : 299, "id" : 1}

@app.route("/")
def hello():
    q = request.args.get('q')
    print(q)
    return {"message" : "Hello"}, 201

@app.route('/book', methods=['POST','GET', 'PUT'])
def book():
    if request.method == 'POST':
        body = request.get_json()
        books.append(body)
        return {"message": "Book already add to database","body": body}, 201
    elif request.method == 'GET':
        return {"books" : books}, 200
    elif request.method == 'PUT':
        body = request.get_json()
        #loop find value
        for i, book in enumerate(books): #enumerate function loop ;loop index and value
            if book['id'] == body['id']:
                book[i] = body
        return {"message" : "Book has been replace", "body" : body}, 200



if __name__ == '__main__':
    app.run(debug=True)