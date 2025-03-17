def binary_search_while(target):
    left = 0
    right = len(li_A) - 1
    state = 'None'  # 직전에 왼쪽 구간을 선택: 'l', 오른쪽 구간을 선택: 'r'로 업데이트

    while left <= right:
        mid = (left + right) // 2

        if li_A[mid] == target:  # 종료 조건
            return 1  # mid index 에서 검색 완료!

        if target < li_A[mid] and state != 'l':
            state = 'l'
            right = mid - 1
        elif target > li_A[mid] and state != 'r':
            state = 'r'
            left = mid + 1
        else:  # 왼왼 or 오오 -> 조건 만족 X
            return 0

    return 0  # li_A에 원하는 요소가 없는 경우


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    li_A = list(map(int, input().split()))
    li_B = list(map(int, input().split()))

    li_A.sort()

    cnt = 0  # 조건을 만족하는 정수의 개수
    for i in li_B:
        result = binary_search_while(i)
        if result:
            cnt += 1
    print(f'#{tc} {cnt}')