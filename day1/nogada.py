import os

# SSAFY지원자 폴더로 들어간다.
os.chdir(r"SSAFY지원자")
# SSAFY지원자 폴더로 들어간다.
os.chdir(r"SSAFY지원자")
# 내용 모두 출력
files = os.listdir()
print(files)

for f in files:
    os.rename(f, f.replace("SAMSUNG", "SSAFY"))
    