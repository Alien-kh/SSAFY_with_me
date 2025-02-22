# 백준 10811
N, M = map(int, input().strip().split())  # 5 4
arr = [a for a in range(0, N+1)]
# M개의 줄에 걸쳐 input이 주어짐
for _ in range(M):
    i, j = map(int, input().strip().split())
    arr[i:j+1] = arr[j:i-1:-1]
# arr.pop(0)
# print(*arr)
print(*arr[1:N+1])