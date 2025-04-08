N, value = map(int, input().split())
lst = [int(input()) for _ in range(N)]  # 리스트를 한 줄로 입력받기

def solve(value):
    cnt = 0
    lst.sort(reverse=True)  # 내림차순 정렬

    for coin in lst:
        if value == 0:
            break
        cnt += value // coin
        value %= coin  # 나머지 갱신

    return cnt

result = solve(value)
print(result)