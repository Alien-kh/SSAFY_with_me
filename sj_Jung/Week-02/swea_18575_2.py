testcase = int(input())

for tc_idx in range(1, testcase + 1):
    square_len = int(input()) # 풍선 가로세로 길이

    sq_num_list = []

    for _ in range(square_len): # 리스트 저장
        num_input = list(map(int, input().split()))
        sq_num_list.append(num_input)

    sum_list = []

    for v_idx in range(square_len):
        for h_idx in range(square_len):
            h_sum = sq_num_list[v_idx][h_idx] # 중앙값
            if v_idx > 0:
                for up in range(v_idx-1, -1, -1): # 위
                    up_num = sq_num_list[up][h_idx]
                    h_sum += up_num
            if v_idx < square_len :
                for down in range(v_idx+1, square_len): # 아래
                    down_num = sq_num_list[down][h_idx]
                    h_sum += down_num
            if h_idx > 0:
                for left in range(h_idx-1, -1, -1): # 좌
                    left_num = sq_num_list[v_idx][left]
                    h_sum += left_num
            if h_idx < square_len :
                for right in range(h_idx+1, square_len): # 우
                    right_num = sq_num_list[v_idx][right]
                    h_sum += right_num
            sum_list.append(h_sum) # 한 점의 상하좌우 값에 중앙값 더한 값을 리스트에 추가
            h_sum = 0

    max_sum = 0
    for idx in range(len(sum_list)): # 리스트 내 최대값 구하기
        if max_sum < sum_list[idx]:
            max_sum = sum_list[idx]

    min_sum = 10000000000
    for idx in range(len(sum_list)): # 리스트 내 최소값 구하기
        if min_sum > sum_list[idx]:
            min_sum = sum_list[idx]
    final = max_sum - min_sum # 최댓값 - 최소값

    print(f'#{tc_idx} {final}')