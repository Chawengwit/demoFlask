#GET Method
from flask import Flask, request

app = Flask(__name__)
#---------------------
@app.route("/") #Define URL's user
def hello():
    #sent query
    q = request.args.get('q') #get Query parameter
    print(q)
    return "Hello!!!", 201 # Create Status 201


if __name__ == '__main__':
    app.run(debug=True)