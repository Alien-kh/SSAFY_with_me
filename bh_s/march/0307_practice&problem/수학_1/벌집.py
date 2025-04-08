# 벌집문제. 벌집은 초기 기준 6*n 만큼 다음 방 라인이 늘어난다. 그럼 n + 1 을 반환하면?

def solve(n):
    if n == 1:
        return 1

    cnt = 1
    value = 1
    while value < n:
        value += 6 * cnt
        cnt += 1

    return cnt


num = int(input())
print(solve(num))

