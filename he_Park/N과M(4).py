# 중복 조합 문제

N, M = map(int, input().split())
path = []
def recur(start, cnt):

    if cnt == M:
        print(*path)
        return

    for i in range(start, N + 1):
        path.append(i)
        recur(i, cnt + 1)
        path.pop()


recur(1, 0)

