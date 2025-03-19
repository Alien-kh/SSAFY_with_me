# 실패
N = int(input())
data = list(map(int, input().split()))

stack = []

i = 0
j = 0
while i != N:
    if data[i] == 1 + j:
        j += 1
    else:
        stack.append(data[i])

    i += 1

stack1 = stack[:]
stack1.sort(reverse=True)

if stack == stack1:
    print('Nice')
else:
    print('Sad')