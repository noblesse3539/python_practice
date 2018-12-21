import random
"""
난이도* 1. 지역(location)은 몇개 있나요?
출력예시)
4
난이도** 2. python standard library에 'requests'가 있나요?
출력예시)
false
난이도** 3. dj1반의 반장의 이름을 출력하세요.
출력예시)
박성민
난이도*** 4. ssafy에서 배우는 언어들을 출력하세요.
출력 예시)
python
web
난이도*** 5 ssafy dj2의 강사와 매니저의 이름을 출력하세요.
출력 예시)
junho
pro2
난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요.
출력 예시)
flask는 micro이다.
django는 full-functioning이다.
난이도***** 7. 오늘 당번을 뽑기 위해 groups의 3조 중에 한명을 랜덤으로 뽑아주세요.
출력예시)
오늘의 당번은 고병석
"""
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "dj1":  {
            "lecturer": "tak",
            "manager": "pro1",
            "class president": "박성민",
            "groups": {
                "1조": ["강신욱", "윤영우", "이민교", "유창오", "황여진", "김민경"],
                "2조": ["노승만", "이재찬", "이주호", "김예지", "유지원"],
                "3조": ["이민지", "김희윤", "박성민", "조인정", "김슬기", "고병석"],
                "4조": ["임동명", "김승훈", "정상영", "정태현", "한단비", "김동민"]
            }
        },
        "dj2": {
            "lecturer": "junho",
            "manager": "pro2"
        }
    }
}

# 1.  지역(location)은 몇개 있나요?
loc = ssafy["location"]
print(len(loc))

# 2. python standard library에 'requests'가 있나요?
print("requests" in ssafy["language"]["python"]["python standard library"])

# 1) 조건, 반복문으로만 할 때
# py_library = ssafy["language"]["python"]["python standard library"]
# is_requests = False
# for library in py_library:
#     if "requests" == library:
#         is_requests = True
# print(is_requests)

# 3. dj1반의 반장의 이름을 출력하세요.
print(ssafy["classes"]["dj1"]["class president"])

# 4. ssafy에서 배우는 언어들을 출력하세요.
for lang in ssafy["language"].keys():
    print(lang)
# a[].keys()
# a[].values()
# a[].items()

# 5 ssafy dj2의 강사와 매니저의 이름을 출력하세요.
dj2 = ssafy["classes"]["dj2"]
for name in dj2.values():
    print(f"{name}")

# 6. framework들의 이름과 설명을 다음과 같이 출력하세요.

frameworks = ssafy["language"]["python"]["frameworks"]
for name, func in frameworks.items():
    print(f"{name}는 {func}이다.")

# 7. 오늘 당번을 뽑기 위해 groups의 3조 중에 한명을 랜덤으로 뽑아주세요.
team3List = ssafy["classes"]["dj1"]["groups"]["3조"]
who = random.choice(team3List)
print(f"오늘의 당번은 {who}!!!")