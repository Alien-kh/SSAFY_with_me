import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    C = sys.stdin.readline().split()
    if C[0] == '1':
        stack.append(C[1])
    elif C[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif C[0] == '3':
        print(len(stack))
    elif C[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif C[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)

