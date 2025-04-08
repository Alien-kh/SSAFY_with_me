import sys

for line in sys.stdin:
    print(line.strip())

# sys.stdin은 입력이 끝날때까지 계속 읽어옴
# 입력값의 갯수를 모를때에는 sys.stdin 사용