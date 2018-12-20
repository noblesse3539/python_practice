from flask import Flask,render_template
import datetime
import requests
app = Flask(__name__)

# 0. 요청 url 만들기
key = "95db8b538a03334956d1569a913979bd"
targetDt = "20181013"


urlDict = {
    "일별박스오피스" : "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json",
    "주간주말박스오피스" : "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json",
    "공통코드조회" : "http://www.kobis.or.kr/kobisopenapi/webservice/rest/code/searchCodeList.json",
    "영화목록" : "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json",
    "영화상세정보" : "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json",
    "영화사목록" : "http://www.kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyList.json",
    "영화사상세정보" : "http://www.kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyInfo.json",
    "영화인목록" : "http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json",
    "영화인상세정보" : "http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleInfo.json"
}

url = f"{urlDict['일별박스오피스']}?key={key}&targetDt={targetDt}&"

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/movierank")
def movierank():
    today = datetime.date.today()
    targetDt = str(today.year)+str(today.month)+str(today.day)
    url = f"{urlDict['일별박스오피스']}?key={key}&targetDt={targetDt}&"
    response = requests.get(url).json()
    movielist = []
    for i in response["boxOfficeResult"]["dailyBoxOfficeList"]:
        movielist.append(i["movieNm"])
    return render_template("movierank.html", movielist=movielist)
