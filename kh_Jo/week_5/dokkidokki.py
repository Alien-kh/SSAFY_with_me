n = int(input())
j = list(map(int, input().split()))
stack = []
count =1
can_eat = True
for num in j:
    while stack != [] and stack[-1] == count:
        stack.pop()
        count+=1
    if num == count:
        count +=1
    else:
        stack.append(num)
for _ in range(len(stack)):
    a = stack.pop()
    if a == count:
        count +=1
        continue
    else:
        can_eat = False
        break
if can_eat:
    print("Nice")
else:
    print("Sad")