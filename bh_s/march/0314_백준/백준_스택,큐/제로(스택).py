K = int(input())
stack = []
for i in range(K):
    data = int(input())
    if data == 0:
        stack.pop()
    else:
        stack.append(data)

print(sum(stack))
