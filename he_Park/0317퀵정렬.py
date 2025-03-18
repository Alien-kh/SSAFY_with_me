def partitioning(left, right):
    mid = (left + right) // 2
    pivot = data[mid]  # 피벗을 중간 요소로 설정
    data[left], data[mid] = data[mid], data[left]

    i = left + 1
    j = right

    while i <= j:
        while i <= j and data[i] <= pivot:
            i += 1
        while i <= j and data[j] >= pivot:
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]

    data[left], data[j] = data[j], data[left]
    return j

def quick_sort(left, right):
    if left < right:
        pivot = partitioning(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    quick_sort(0, N - 1)

    print(f'#{tc} {data[N//2]}')