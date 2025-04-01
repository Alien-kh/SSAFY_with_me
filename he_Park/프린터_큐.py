#풀다 말았다
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    if N == 1:
        priority = [int(input())]
    else:
        priority = list(map(int, input().split()))

    arr = []

    for i in range(N):
        arr.append((priority[i], i))  # i번째 문서의 중요도, i번째 문서

    cnt = 0

    