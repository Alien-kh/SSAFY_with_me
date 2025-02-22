from collections import deque
N = int(input())
T  = int(input())
arr = deque(list(map(int,input().split())))
num = list(map(int,input().split()))
for i in range(T):
    for j in range(num[i]-1):
        a = arr.popleft()
        arr.append(a)
    print(arr[0], end = " ")
    
    