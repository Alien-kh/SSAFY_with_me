# 5개의 자연수가 주어질 때, 가운데 있는 수 출력하기.

def insert_sort(data):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key: # 왼쪽에서 key 보다 큰 값이 있다면.
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key


data = []
for _ in range(5):
    num = int(input())
    data.append(num)

insert_sort(data)
print(int(sum(data)/len(data)))
print(data[2])
