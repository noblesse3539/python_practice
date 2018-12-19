import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/feed/trending"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(type(soup))