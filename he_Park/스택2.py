import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    data = input().split()  # 리스트로 받음
    if data[0] == '1':
        stack.append(data[1])
    if data[0] == '2':
        print(stack.pop()) if stack else print(-1)
    if data[0] == '3':
        print(len(stack))
    if data[0] == '4':
        print(1) if not stack else print(0)
    if data[0] == '5':
        print(stack[-1]) if stack else print(-1)