def solve(arr, N):
    # 첫 번째 '#' 찾기
    found = False
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                start_row, start_col = i, j
                found = True
                break
        if found:
            break
    #가로로 연속된 # 계산
    col_count = 0
    temp_col = start_col # i부터 시작하는 변수를 만들어줘서
    while temp_col< N and arr[start_row][temp_col] == '#':
        col_count +=1
        temp_col +=1 # 점차 변수를 증가 시켜 #의 종점이 어디있는 지 확인

    #세로로 연속된 # 계산
    row_count = 0
    temp_row = start_row
    while temp_row < N and arr[temp_row][start_col] == '#':
        row_count +=1
        temp_row +=1
    if row_count != col_count:
        return 'no'
    # 정사각형 안에 #이 전부 들어가있는 지 확인
    for i in range(start_row, start_row+row_count): #시작 점부터 가로의 개수를 더해ㅜ고
        for j in range(start_col, start_col + col_count): # 세로의 개수를 더해줘서 각 항에 전부 #이 들어가있는지 (정사각형인지 확인)
            if arr[i][j] != '#':
                return 'no'

    # 정사각형 밖에 #이 있는지 확인
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#' and not(start_row<= i < start_row +row_count and start_col<=j < start_col+ col_count):
                return 'no'
    return 'yes'








T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    print(f'{tc} {solve(arr, N)}')


# def solve(arr, N):
#     # 초기값 설정: 최소값은 큰 값, 최대값은 작은 값으로 초기화
#     min_row, max_row = N, -1
#     min_col, max_col = N, -1
#     total = 0  # '#'의 총 개수

#     # 격자판 한 번 순회하며 '#'의 위치 파악
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == '#':
#                 total += 1
#                 min_row = min(min_row, i)
#                 max_row = max(max_row, i)
#                 min_col = min(min_col, j)
#                 max_col = max(max_col, j)
                
#     # 문제에서는 최소 1개의 '#'이 있다고 했으므로 total == 0 인 경우는 고려하지 않아도 됨

#     # 바운딩 박스의 높이와 너비 계산
#     height = max_row - min_row + 1
#     width = max_col - min_col + 1

#     # 1. 정사각형 조건: 높이와 너비가 같아야 함
#     # 2. '#'의 총 개수가 정사각형의 면적과 일치해야 함
#     if height != width or total != height * width:
#         return 'no'
        
#     return 'yes'


# # 입력 및 출력 처리
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(input().strip()) for _ in range(N)]
#     print(f'{tc} {solve(arr, N)}')