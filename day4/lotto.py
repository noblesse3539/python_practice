import requests
import random
# 1. https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=400
# 위의 주소로 요청을 보낸다.

url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=400"

response = requests.get(url)


# 2. 응답된 결과를 json으로 바꿔서 dictionary처럼 활용한다.
lotto_numbers = response.json()

win_number = []
for i in range(1,7):
    win_number.append(lotto_numbers[f"drwtNo{i}"])

win_number = list(map(int, win_number))
win_number = sorted(win_number)

bonus_number = int(lotto_numbers["bnusNo"])
# print("당첨번호:",win_number, "보너스번호:", bonus_number)
# 3. 랜덤으로 로또 번호 하나를 추출한다.
myNum = random.sample(range(1,46), 6)
myNum.sort()
# print("내  번호:", myNum)
# 4. 몇 등인지 알아본다.
# cnt = 0
# bonusCnt = 0
# for i in myNum:
#     if i in win_number:
#         cnt = cnt + 1
#     if i == bonus_number:
#         bonusCnt += 1

# print("맞은 갯수:", cnt, "보너스맞은 갯수:", bonusCnt)

# if cnt == 6:
#     print("1등!")
# elif cnt == 5:
#     if bonusCnt == 1:
#         print("2등!")
#     else :
#         print("3등!")
# elif cnt == 4:
#     print("4등!")
# elif cnt == 3:
#     print("5등!")
# else :
#     print("꽝!!!")
# # 1등 : 6개, 2등 : 5개 + 보너스 번호
# # 3등 : 5개, 4등 : 4개, 5등 : 3개

'''
파이썬에는 set이라는 자료형이 있다.
list를 set으로 형변환을 할 수 있다.
혹은 a = {1, 2, 5} 직접 만들 수도 있다.

set은 중복된 값을 제거한다.
예) a = [1,2,2]
set(a)
=> {1,2}

교집합(&), 차집합(-), 합집합(|)을 할 수 있다.

'''
lucky = [0,0,0,0,0]
for i in range(100000000):
    myNum = random.sample(range(1,46), 6)
    matched = len(set(win_number) & set(myNum))
   
    if matched == 6:
        lucky[0] += 1
        break
    elif matched == 5 and bonus_number in myNum :
        lucky[1] += 1
    elif matched == 5:
        lucky[2] += 1
    elif matched == 4:
        lucky[3] += 1
    elif matched == 3:
        lucky[4] += 1
    print(lucky, i, end="\r")
