from flask import Flask, request

app = Flask(__name__)

foods = [
    {"id" : 1,"name" : "Momo Paradize"}, 
    {"id" : 2,"name" : "Shinkanzen Sushi"}, 
    {"id" : 3,"name" : "ส้มตำลุงหนวด"}, 
    {"id" : 4,"name" : "หมูกระทะ"}, 
    {"id" : 5,"name" : "Jones Salad"},
    {"id" : 6,"name" : "ขนมจีน แกงเขียวหวาน"},
    {"id" : 7,"name" : "หมูสะเต๊ะ"},
    {"id" : 8,"name" : "ผัดไทย"},
    {"id" : 9,"name" : "เจ้โอว"} ,
    {"id" : 10,"name" : "ทุเรียน"}
]

@app.route('/foods',methods=['POST','GET','PUT','DELETE'])

def food():
    if request.method == 'POST':
        body = request.get_json()
        foods.append(body)
        return {"message" : "Your food is already add to database","body":body},201
    elif request.method == 'GET':
        return {"Foods !! : ": foods}, 200
    elif request.method == 'PUT':
        body = request.get_json()
        for i, food in enumerate(foods):
            if food['id'] == body['id']:
                food[i] = body
        return {"message" : "Food has been updated", "body": body}, 200
    elif request.method == 'DELETE':
        delID = request.get_json()
        for i, food in enumerate(foods):
            if foods['id'] == int(delID):
                foods.pop(i)
        return {"message" : "Food has been deleted !"}, 200
    else:
        pass


if __name__ == '__main__':
    app.run(debug=True)
