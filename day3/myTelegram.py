import json
import requests
from bs4 import BeautifulSoup
import os
#토큰은 비밀번호와 같다. 주의 또 주의
token = os.getenv("TELEGRAM_TOKEN")
url = f"https://api.telegram.org/bot{token}/getMe"

# getUpdates의 내용을 가져와서 dict에 저장하기
updatesURL = f"https://api.telegram.org/bot{token}/getUpdates"

getUpdatesURL = requests.get(updatesURL)
jsonToDict = json.loads(getUpdatesURL.text)
# print(type(jsonToDict))
print(type(jsonToDict["result"]))
lst = jsonToDict["result"]
recentSender = lst[len(lst)-1]
user_id = recentSender["message"]["from"]["id"]
givedmsg = recentSender["message"]["text"]
# print(givedmsg)
# print(user_id)
msg = givedmsg
url = f"https://api.telegram.org/bot{token}/sendMessage?text={msg}&chat_id={user_id}"

requests.get(url)