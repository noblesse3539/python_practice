import requests
from bs4 import BeautifulSoup
url = "https://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser" )

real = soup.select(".roll_txt")
for tag in real:
    word = tag.select(".link_issue")[0].text
    print(word)
