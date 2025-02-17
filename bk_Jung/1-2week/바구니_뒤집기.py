N,M = map(int,input().split())
arr = [i+1 for i in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    arr[a-1:b] = list(reversed(arr[a-1:b]))


for i in arr:
    print(i, end = " ")
