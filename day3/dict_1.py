phonebook = {
    "중국집": "02821",
    "초밥집": "031",
    "한식집": "052"
}


phonebook2 = dict(중국집=1, 초밥집= 2)

print(type(phonebook2))
print(phonebook)
print(phonebook2)

phonebook["분식집"] = "12345"
print(phonebook["분식집"])


# 1. 좋아하는 그룹에 : key - 이름 value : 나이

coldplay = dict(크리스마틴 = 20, 조니버클랜드=21, 가이베리맨=22, 윌챔피언=23)

#1-2. idol이라는 dictionary
#idol - key: 그룹명, value: dictionary

idol = {
    "블랙핑크": {
        "지수" : 20,
        "제니" : 21,
        "로제" : 22,
        "리사" : 23
    },
    "god" : {
        "박준형" : 30,
        "윤계상" : 31,
        "데니안" : 32,
        "손호영" : 33,
        "김태우" : 34
    }

}

# dictionary 반복문
for key in phonebook:
    print(key, phonebook[key])
    #print(key, end=' ')
    #print(phonebook[key])

# key, value 
for key, value in phonebook.items():
    # for key, value => key에 key가 들어간다 ㅋㅋㅋ
    print(key, value)

# value
for value in phonebook.values():
    print(value)

# key
for key in phonebook.keys():
    print(key)