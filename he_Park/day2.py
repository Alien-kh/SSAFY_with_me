# 백준 25304

X = int(input())
N = int(input())

total_receipt = 0

for _ in range(N):
    a, b = map(int, input().split())
    total_receipt += a * b

if total_receipt == X:
    print('Yes')
else:
    print('No')