# 버블 정렬 함수 구현

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:  # 인접한 두 수를 비교하여 교환
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [5, 1, 3, 7, 2, 9]
bubble_sort(arr)
print(arr)