# 카운팅 배열.

lst = [0]*31

for _ in range(28):
    data = int(input())
    lst[data] = 1

for i in range(1,31):
    if lst[i] != 1:
        print(i)
