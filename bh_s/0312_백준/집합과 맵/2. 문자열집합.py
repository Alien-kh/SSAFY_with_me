# 첫줄에 N, M 이 주어지고
# 그 이후로 N개 줄에 집합 S의 문자열, M개 줄에 검사해야할 문자열

N, M = map(int, input().split())
S = set()
cnt = 0
for _ in range(N):
    ch = input()
    S.add(ch)
for i in range(M):
    ch2 = input()
    if ch2 in S:
        cnt += 1

print(cnt)
