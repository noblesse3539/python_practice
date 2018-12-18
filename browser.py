import webbrowser
starList = ['콜드플레이', '아이유', '검정치마']
url = "https://google.com/search?q="
for i in starList:
    webbrowser.open(f"{url}{i}")
