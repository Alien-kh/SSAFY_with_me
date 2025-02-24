from collections import deque

N,K = map(int,input().split())
arr = [i for i in range(1,N+1)] # N번까지 배열 생성
arr =deque(arr)


result = []
while arr:
    arr.rotate(-K+1)
    result.append(arr.popleft())

print('<',end ="")
for i in range(len(result)-1):
    print(f'{result[i]},',end = " ")

print(result[-1],end ="")
print('>')
         