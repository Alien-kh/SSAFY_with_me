N = int(input())
arr = [[0 for _ in range(100)] for _ in range(100)]

for i in range(N):
    a,b = map(int,input().split())
    for j in range(10):
        for k in range(10):
            arr[a+j][b+k] +=1
result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] > 0:
            result +=1

print(result)        
