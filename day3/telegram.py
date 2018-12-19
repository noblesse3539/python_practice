import requests
import os
#토큰은 비밀번호와 같다. 주의 또 주의
token = os.getenv("TELEGRAM_TOKEN")
print(token)
url = f"https://api.telegram.org/bot{token}/getUpdates"

# 1. 요청을 보낸 결과를 response 저장을 한다.
response =  requests.get(url)


# 2. json 형식으로 바꾼다.

updates = response.json()
# 지금은 dictionary와 list가 섞여 있는 것과 같다고 생각하자!


# 3. user의 id를 찾는다.
# print(updates)
currentResult = len(updates["result"])-1

user_id = updates["result"][currentResult]["message"]["from"]["id"]

# 4. 메시지를 설정한다.
msg = updates["result"][currentResult]["message"]["text"]


# 5. 메시지를 보낸다.

url = f"https://api.telegram.org/bot{token}/sendMessage?text={msg}&chat_id={user_id}"

requests.get(url)

# vi ~/.bash_profile
#alias python='winpty python.exe'
