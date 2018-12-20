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
# win_number = sorted(win_number)

bonus_number = int(lotto_numbers["bnusNo"])
print("당첨번호:",win_number, "보너스번호:", bonus_number)
# 3. 랜덤으로 로또 번호 하나를 추출한다.


def countNum(win_number, bonus_number, myNum) :
    cnt = 0
    bonusCnt = 0
    for i in myNum:
        if i in win_number:
            cnt = cnt + 1
        if i == bonus_number:
            bonusCnt += 1
    return cnt, bonusCnt

def winResult(cnt, bonusCnt) :
    if cnt == 6:
        print("1등!")
        return True
    elif cnt == 5:
        if bonusCnt == 1:
            print("2등!")
            return False
        else :
            print("3등!")
            return False
    elif cnt == 4:
        print("4등!")
        return False
    elif cnt == 3:
        print("5등!")
        return False
    else :
        print("꽝!!!")
        return False

def creatNum() :
    myNum = random.sample(range(1,46), 6)
    return myNum
# 1등 : 6개, 2등 : 5개 + 보너스 번호
# 3등 : 5개, 4등 : 4개, 5등 : 3개

win = False
cnt = 0
while not win :
    cnt = cnt + 1
    myNum = creatNum()
    print("내  번호:", myNum)
    eqcnt, luckcnt = countNum(win_number, bonus_number, myNum)
    print("맞은 갯수:", eqcnt, "보너스맞은 갯수:", luckcnt)
    win = winResult(eqcnt, luckcnt)

print(f"1등 당첨까지 시도 한 횟수 : {cnt}")
