def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:  # 왼쪽에서 key보다 큰 값을 오른쪽으로 이동
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # 올바른 위치에 key 삽입