"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}




# 답변 코드는 아래에 작성해주세요.
print("=====Q1=====")
total = sum(iu_score.values())
print(total/len(iu_score))

# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}

# 답변 코드는 아래에 작성해주세요.

print("=====Q2=====")
sumOfScore = 0
numOfScore = 0
for dict in score.values():
    for value in dict.values():
        sumOfScore += value
        numOfScore += 1

print(sumOfScore/numOfScore)

# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
city = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q3=====")
for city1, tempList in city.items():
    evr = 0
    for value in tempList:
        evr += value
    evr /= len(tempList)
    print(city1, evr)






# 답변 코드는 아래에 작성해주세요.
print("=====Q3-1=====")
for city1, tempList in city.items():
    sortedList = sorted(tempList)
    # print(f"{city1} : max - {sortedList[len(sortedList)-1]}, min - {sortedList[0]}")
    print(f"{city1} - max : {list(reversed(sortedList))[0]}, min : {sortedList[0]}")


# 답 예시
cold = 0
hot = 0
cnt = 0
hot_city = ""
cold_city = ""
for name, temp in city.items():
    if cnt == 0:
        hot_city = name
        cold_city = name
        hot = max(temp)
        cold = min(temp)
    else :
        if hot < max(temp) :
            hot = max(temp)
            hot_city = name
        if cold > min(temp) :
            cold = min(temp)
            cold_city = name
    cnt += 1
print (f"가장 더운 도시 : {hot_city} , 가장 추운 도시 : {cold_city}")

# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
print("=====Q4=====")
if ( 2 in city["서울"] ):
    print("네")
else :
    print("아니오")