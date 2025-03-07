import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]

max_v = -1
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_v:
            max_v = max(max_v, arr[i][j])
            r, c = i+1, j+1

print(max_v)
print(r, c)