# N = int(input())
# points = [list(map(int, input().split())) for _ in range(N)]
#
# points.sort()  # 기본적으로 (x, y) 순으로 정렬됨
#
# for x, y in points:
#     print(x, y)
# 가장 빠른 해답.

# 내가 한번 해보는 quick 정렬.


def quick_sort(arr, left, right):
    if left >= right:
        return

    pivot = arr[left]  # 첫 번째 원소를 피벗으로 선택
    l, r = left + 1, right

    while l <= r:
        while l <= right and (arr[l][0] < pivot[0] or (arr[l][0] == pivot[0] and arr[l][1] < pivot[1])):
            l += 1
        while r > left and (arr[r][0] > pivot[0] or (arr[r][0] == pivot[0] and arr[r][1] > pivot[1])):
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]

    arr[left], arr[r] = arr[r], arr[left]  # 피벗을 정렬된 위치로 이동
    quick_sort(arr, left, r - 1)  # 왼쪽 부분 정렬
    quick_sort(arr, r + 1, right)  # 오른쪽 부분 정렬


N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

quick_sort(points, 0, N - 1)

for x, y in points:
    print(x, y)

