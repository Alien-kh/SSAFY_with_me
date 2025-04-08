# N개의 수가 주어질 때, 오름차순으로 정렬

def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


N = int(input())
data = []
for i in range(N):
    num = int(input())
    data.append(num)

bubble_sort(data)
for n in range(N):
    print(data[n])
