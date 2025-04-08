import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
min_v = 1000001
max_v = -1000001
for i in range(len(data)):
    if data[i] > max_v:
        max_v = data[i]
    if data[i] < min_v:
        min_v = data[i]

print(f'{min_v} {max_v}')

#   print(min(data),max(data))