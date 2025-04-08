arr = [input().strip() for _ in range(5)]

# 문자열의 길이가 다르기에 그 중 가장 긴 것의 길이로 접근
max_len = max(len(s) for s in arr)

# 세로로 읽어서 문자열 만들기.
result = ""
for col in range(max_len):
    for row in range(5):
        # 현재 행의 열이 존재 하는가? len(arr[row]) = 현재 행의 길이(열의 개수)
        if col < len(arr[row]):
            result += arr[row][col]

print(result)
