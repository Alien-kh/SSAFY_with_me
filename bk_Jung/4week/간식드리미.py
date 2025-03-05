import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
treshold = N + 1
stack = []
num = 1
for i in L:
    stack.append(i)
    if stack[-1] == num:
        stack.pop()
        num += 1
        if len(stack) != 0 and num != treshold:
            for i in range(len(stack)):
                if stack[-1] == num:
                    stack.pop()
                    num += 1
    elif num == treshold:
        break

if num == treshold:
    print('Nice')
else:
    print('Sad')