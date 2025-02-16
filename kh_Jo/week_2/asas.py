arr = []
for _ in range(5):
    arr.append(list(input()))

max_length = max(len(row) for row in arr)
result_lst = []
for i in range(5):
    while len(arr[i]) < max_length:
        arr[i].append('')
# print(arr)

for i in range(max_length):
    for j in range(len(arr)):
        if i < len(arr[j]):
            result_lst.append(arr[j][i])
print(''.join(result_lst))
