# 리스트의 요소를 비교하는 방법.

lst = [0]*10
cnt_lst = []

for i in range(10):
    data = int(input())
    lst[i] = data % 42

for num in lst:
    if num not in cnt_lst:
        cnt_lst.append(num)

print(len(cnt_lst))
