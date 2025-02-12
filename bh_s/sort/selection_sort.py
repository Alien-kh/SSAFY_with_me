def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i  # 현재 정렬할 위치
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:  # 최소값 찾기
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 위치 교환
    return arr

arr = [5, 1, 3, 7, 2, 9]
selection_sort(arr)
print(arr)