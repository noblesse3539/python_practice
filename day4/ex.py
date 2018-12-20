'''
문제 1.
문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
'''

str = input('문자를 입력하세요: ')
# 아래에 코드를 작성해 주세요.
print(str[0], str[-1])
'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

n = int(input('숫자를 입력하세요: '))
# 아래에 코드를 작성해 주세요.
for i in range(1, n+1) :
    print(i)
'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('숫자를 입력하세요: '))
# 아래에 코드를 작성해 주세요.
if number % 2:
    print(number, "는 홀수 입니다.")
else :
    print(number, "는 짝수 입니다.")
'''
문제 4.
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
국어는 90점 이상,
영어는 80점 초과,
수학은 85점 초과, 
과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 
'''

a = int(input('국어: '))
b = int(input('영어: '))
c = int(input('수학: '))
d = int(input('과학: '))
# 아래에 코드를 작성해 주세요.
print(a >= 90 and b > 80 and c > 85 and d >= 80)

'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

prices = input('물품 가격을 입력하세요: ')
# 아래에 코드를 작성해 주세요.
priceList = prices.split(";")
# 정수로 변환 하는 법 1.
intList = []
for i in priceList:
    intList.append(int(i))
intList.sort()
intList.reverse()
print(intList)

# 정수로 변환 하는 법 2.
# map(int, priceList) map은 첫번째 인자에 함수를 넣으면 두번째 인자의 list 등을 돌면서 함수를 실행해준다. 즉, int 뿐만아니라 print도 되고, 등등

# 정렬 하는 법
#intList.sort()
#prices_int = sorted(prices_int, reverse=True) 이렇게 하면 내림차순으로 정렬됨