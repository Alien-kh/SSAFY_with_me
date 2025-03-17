def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    # 리스트를 두 부분으로 나누기
    mid = len(arr) // 2
    left, left_count = merge_sort(arr[:mid])
    right, right_count = merge_sort(arr[mid:])

    # 두 리스트 병합하기
    merge_lst, merge_count = merge(left, right)

    # 좌측 자른것에서 발생한 경우 + 우측 자른것에서 발생한 경우 + 최종 병합에서 발생한 경우
    total_count = left_count + right_count + merge_count
    
    # 병합한 리스트와 병합 과정에서 발생한 경우의 수 합쳐서 반환.
    return merge_lst, total_count


def merge(left, right):
    result = []
    i = j = 0
    count = 0

    # 병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 확인
    if left and right and left[-1] > right[-1]:
        count += 1

    # 두 리스트를 비교하여 작은 값을 result 에 넣기
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 원소가 있다면 result 에 추가
    result.extend(left[i:])
    result.extend(right[j:])

    return result, count


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    sort_data, total_cnt = merge_sort(data)

    # 중간값(sort_data[N // 2]) , 왼쪽 마지막 원소 > 오른쪽 마지막 원소 인 경우의 수 출력
    print(f'#{tc} {sort_data[N // 2]} {total_cnt}')
