def binary_search_while(target, arr):
    left = 0
    right = len(arr) - 1
    cnt = 0
    curr = None # 왼쪽, 오른쪽으로 어디로 갔는지 판단
    while left <= right:
        mid = (left + right) // 2
        cnt += 1        # 검색횟수 추가


        if arr[mid] == target:
            return mid, cnt, True      # mid index 에서 검색 완료!

        # 왼쪽에 정답이 있다.
        if target < arr[mid]:
            if curr == 'L':
                return False
            right = mid - 1
            curr = 'L'
        else:
            if curr == 'R':
                return False
            left = mid + 1
            curr = 'R'

    return False

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # A와 B에 속한 정수의 개수
    A_lst = list(map(int,input().split()))
    A_lst.sort()# 이걸 뺴먹었다 문제의 조건을 잘보자
    B_lst = list(map(int,input().split()))
    prob_condition_cnt = 0 # 조건에 맞는 것들 세주기
    for num in B_lst:
        right_cnt = 0
        left_cnt = 0
        result = binary_search_while(num, A_lst)
        if result:
            prob_condition_cnt += 1
    print(f'#{tc} {prob_condition_cnt}')
'''
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5
'''

