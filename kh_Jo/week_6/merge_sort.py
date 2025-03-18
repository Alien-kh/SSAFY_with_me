# 1. 분할: 리스트의 길이가 1일 때까지 분할
# 2. 정복: 리스트의 길이가 1이 되면 자동으로 정렬됨
# 3. 병합
#   - 왼쪽, 오른쪽 리스트 중
#       작은 원소부터 정답 리스트에 추가하면서 진행
def merge(left, right):
    global right_first_count
    # 두 리스트를 병합한 결과 리스트
    result = [0] * (len(left) + len(right))
    l = r = 0

    # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복
    while l < len(left) and r < len(right):
        # 만약 오른쪽 원소가 더 먼저 나온 경우는 ? 왼쪽보다 1이 더큰 상태 일때
        if left[l] <= right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1
    if left[-1] > right[-1]: # 만약 오른쪽 것보다 왼쪽 것이 더 큰 상태라면 오른쪽이 먼저 나옴
        right_first_count +=1

    # 왼쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    # 오른쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result


def merge_sort(li):
    if len(li) == 1:
        return li

    # 1. 절반 씩 분할
    mid = len(li) // 2
    left = li[:mid]    # 리스트의 앞쪽 절반
    right = li[mid:]   # 리스트의 뒤쪽 절반

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    # print(left_list, right_list)
    # 분할이 완료되면
    # 2. 병합
    merged_list = merge(left_list, right_list)
    return merged_list

T = int(input())
for tc in range(1, T+1):
    N = int(input())# 정수의 개수
    arr = list(map(int,input().split()))
    right_first_count = 0 # 오른쪽 먼저 나오는 것 세주기
    sorted_arr = merge_sort(arr)
    print(f'#{tc} {sorted_arr[N//2]} {right_first_count}')
'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''