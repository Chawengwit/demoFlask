#POST Method
from flask import Flask, request

app = Flask(__name__)

books = []

@app.route("/")
def hello():
    q = request.args.get('q')
    print(q)
    return {"message" : "Hello"}, 201

@app.route('/book', methods=['POST','GET'])     #Create Server /book and Create Method
def book():
    if request.method == 'POST':
        #print(request.data) #request .data >> return string b'
        #print(request.get_json()) #request .data >> return dictionary
        body = request.get_json()
        books.append(body)
        return {"message": "Book already add to database","body": body}, 201
    elif request.method == 'GET':
        return {"books" : books}, 200

if __name__ == '__main__':
    app.run(debug=True)