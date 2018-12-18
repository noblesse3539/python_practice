import requests
from bs4 import BeautifulSoup
url = "https://naver.com/"
# 1. 원하는 사이트에 요청을 보낸다.
# 그리고, 그 결과를 저장한다.
response = requests.get(url)
print(type(response))
# print(response.text)

# 2. 원하는 정보를 찾는다.
soup = BeautifulSoup(response.text, 'html.parser')
# 3. select는 CSS의 선택자(selector)를 통해 찾을 수 있다.
# #KOSPI_now : id가 KOSPI_now인 것.
# .up : class가 up인 것.
# CSS에서 id는 문서에서 하나, class는 여러개가 있을 수 있다.

# class1 = soup.

realtime = soup.select(".ah_roll")
sets = realtime[0].select(".ah_k")
for word in sets:
    print(word.text)
    

#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a.ah_a > span.ah_k

