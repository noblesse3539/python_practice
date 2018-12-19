# f = open("new.txt", "w")
# f.write("글써졌니?")
# f.close()

# 1. 파일 쓰기
with open("new1.txt", "w" ) as file:
    '''
    파이썬에서 with는 컨택스트 매니저라고 부른다.
    with 블록내에서 파일을 조작하고,
    블록이 끝나게 되면 파일을 자동으로 닫아준다.
    '''
    file.write("글 또 쓰자")

# 2. 파일 읽기
with open("new.txt", "r") as file:
    line = file.read()
    print(line)

# 3. 파일 여러줄 쓰기
with open("new2.txt", "w") as file:
    for line in range(50):
        file.write(f"{line}번째 줄입니다.\n")

# 4. 여러 줄의 파일 읽기
with open("new2.txt", "r") as file:
    lines = file.readlines()
    # for line in lines:
    #     print(line)

    i = 0
    while i < len(lines):
        print( lines[i])
        i += 1