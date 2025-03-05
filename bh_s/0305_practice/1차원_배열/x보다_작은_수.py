N, X = map(int, input().split())
data = list(map(int, input().split()))
new_lst = []
for i in range(len(data)):
    if data[i] < X:
        new_lst.append(data[i])
print(*new_lst)