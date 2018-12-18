
with open("ssafy.txt", "w") as file:
    file.write("안녕\n하세요\n저는\n김탁희\n입니다\n만나서\n반갑습니다.\n")

with open("result.txt", "w") as in_file:
    # with open("ssafy.txt", "r") as out_file:
    #     lines = out_file.readlines()
    #     line = len(lines) -1
    #     while line >= 0:
    #         in_file.write(f"{lines[line]}")
    #         line -= 1
     with open("ssafy.txt", "r") as out_file:
        lines = out_file.readlines()
        for line in reversed(lines):
            in_file.write(f"{line}")