def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피봇보다 큰 값 찾기
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        # 피봇보다 작은 값 찾기
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:  # 엇갈린 경우 피봇과 작은 값 교체
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:  # 엇갈리지 않은 경우 값 교환
            arr[left], arr[right] = arr[right], arr[left]

    # 재귀 호출
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    quick_sort(data, 0, N - 1)
    print(f'#{tc} {data[N // 2]}')
