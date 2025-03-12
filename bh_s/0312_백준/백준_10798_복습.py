# 문자열 데이터를 받아서 세로로 읽기.

new_chr = ''
data = [list(input().strip()) for _ in range(5)]

length = max(len(s) for s in data)
for c in range(length):
    for r in range(5):
        # 현재 행의 열이 존재하는지 확인. len(data[r]) = 현재 행의 길이(열의 개수)
        if c < len(data[r]):
            new_chr += data[r][c]

print(new_chr)
