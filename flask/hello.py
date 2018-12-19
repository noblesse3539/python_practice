from datetime import date
from flask import Flask, render_template
import random
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

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

@app.route("/dinner")
def dinner():
    # # 1. 저녁 list 만들고
    dinnerList = ["짜장면", "반반치킨", "양념치킨", "후라이드치킨"]
    imgDict = {
        "짜장면" : "http://recipe1.ezmember.co.kr/cache/recipe/2016/07/02/40c4f639ca973d9acccecdf7cbe0cbc41.jpg",
        "반반치킨" : "http://www.cheogajip.co.kr/data/file/menu/thumb-32732614_IS24EQVA_678ab6e730f0dcc0649094f5a519801ae6926956_290x297.png",
        "양념치킨" : "https://img.insight.co.kr/static/2017/12/03/700/83ay2m7551656tdgx4i3.jpg",
        "후라이드치킨" : "https://t1.daumcdn.net/cfile/tistory/2349D53F5833FE8128",
    }
    youtubeDict = {
        "짜장면" : "https://www.youtube.com/embed/rEn2bqPCChA",
        "반반치킨" : "https://www.youtube.com/embed/AL9HVzVb5RI",
        "양념치킨" : "https://www.youtube.com/embed/jhep14W-pqg",
        "후라이드치킨" : "https://www.youtube.com/embed/nCPixGRK3vI" 
    }
    # # 2. 하나 뽑아주세요.
    menu = random.choice(dinnerList)
    menu_url = imgDict[menu]
    youtube_url = youtubeDict[menu]

    return render_template("dinner.html", menu= menu, dinner= dinnerList, menu_url = menu_url, youtube_url = youtube_url)

@app.route("/randomA")
def randomA():
    url = "https://www.youtube.com/feed/trending"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    container = soup.select_one("#grid-container")
    titleList = container.select("#video-title")
    choice = random.choice(titleList)
    return render_template("random.html", titleList = titleList, choice = choice)