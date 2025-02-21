n,m = map(int,input().split())
INF = int(1e9)

graph = [[INF] * (n +1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a ,b = map(int,input().split())
    graph[a][b] = 1

for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][i] + graph[i][b] == 2:
                graph[a][b] = 1

result = [0] * (n+1)

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == 1:
            result[a] += 1
            result[b] += 1
print(result)
print(result.count(n-1))
            