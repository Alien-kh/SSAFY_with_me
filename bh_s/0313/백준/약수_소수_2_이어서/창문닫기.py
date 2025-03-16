import math

N = int(input())

# 완전 제곱수의 개수 구하기
cnt = 0
for i in range(1, int(math.sqrt(N)) + 1):
    if i * i <= N:
        cnt += 1

print(cnt)