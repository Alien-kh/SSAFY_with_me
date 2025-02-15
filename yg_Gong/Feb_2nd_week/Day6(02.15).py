# 풍선팡 보너스 게임
# 얻을 수 있는 보너스 점수의 최댓값과 최솟값의 차이를 구하기

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    col_sum_lst = []    # 열의 합
    row_sum_lst = []    # 행의 합
    max_score = 0   # 보너스 점수에서 얻을 수 있는 최고 점수
    min_score = 100000  # 보너스 점수에서 얻을 수 있는 최저 점수

    # 행별 합을 구함
    for i in range(N):
        row_sum = 0
        for j in range(N):
           row_sum += arr[i][j]
        # 행별로 합산한 값을 리스트에 저장
        row_sum_lst.append(row_sum)

    # 열별 합을 구함
    for j in range(N):
        col_sum = 0
        for i in range(N):
           col_sum += arr[i][j]
        # 행별로 합산한 값을 리스트에 저장
        col_sum_lst.append(col_sum)

    # 터진 풍선 위치에 따른 열과 행의 합산으로 max,min구하기
    for i in range(N):
        for j in range(N):
            bonus_score = row_sum_lst[i] + col_sum_lst[j] - arr[i][j]   # 중복된 터뜨린 풍선 점수 빼기

            if bonus_score > max_score:
                max_score = bonus_score
            if bonus_score < min_score:
                min_score = bonus_score

    result = max_score - min_score

    print(f'#{tc} {result}')