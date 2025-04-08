# N 명에서 점수가 높은 K 명은 상을 받을 것.
def bubble_sort(data):
    n = len(data)
    for i in range(n-1):
        for j in range(n - 1 - i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


N, K = map(int, input().split())
data = list(map(int, input().split()))
bubble_sort(data)
print(data[N-K])
