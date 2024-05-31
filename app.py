from flask import Flask,request
app = Flask(__name__)



@app.route("/drinks")
def drinks():
    drink_no=5
    # return "Cola"+str(drink_no)
    return f"Cola {drink_no} {drink_no}"

@app.route('/drinks/<id>/<x>')
def drinks_id(id, x):
    print(id) 
    return {"output":int(id), "second": x}
# paste: http://localhost:5000/drinks/3/str

@app.route('/drinks',methods=['POST'])
def post_drink():
    print(request.json)
    return request.json

@app.route('/newuser/<name>/<email>',methods=['GET'])
def get(name, email):
    return {"name":name,"email":email}

@app.route('/newuser/',methods=['POST'])
def post():
    data = request.json
    return {"name":data['name'],"email":data['email']}