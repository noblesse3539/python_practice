from datetime import date
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ssafy")
def ssafy():
    return "안녕 싸피!"

@app.route("/isitchristmas")
def christmas():
    today = date.today()

    if today.month == 12 and today.day == 25 :
        return "YES!!!"
    else :
        return "NO..."

# variable routing : 주소로 들어오는 값을 변수로 사용하는거임.
@app.route("/greeting/<string:name>")
def greeting(name):
    return f"{name} 안녕"


@app.route("/cube/<int:num>")
def cube(num):
    return f"{num**3}"