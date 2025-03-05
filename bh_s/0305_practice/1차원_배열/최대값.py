lst = []
max_v = 0
idx = -1
for i in range(0, 9):
    data = int(input())
    lst.append(data)
    if max_v < lst[i]:
        max_v = lst[i]
        idx = i+1

print(max_v)
print(idx)
