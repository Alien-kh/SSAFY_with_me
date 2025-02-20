while True:
    stack = []
    N = input()
    if N[0] == '.':
        break

    for i in N:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')