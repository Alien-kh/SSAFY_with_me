lst = []
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        lst.append(num)

if not lst:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))