N, M = map(int,input().split())
result = [[0] * M for _ in range(N)]
A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(N)]
for num in range(N):
    for j in range(M):
        result[num][j] = A[num][j] + B[num][j]

for row in result:
    print(*row)
