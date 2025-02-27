from itertools import count
'''
1
5 6 2 1 3
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0
'''

def solve(R, C, L):
    d_list = [
        [(0,0), (0,0), (0,0), (0,0)], # 0번 못가
        [(-1,0), (1,0), (0,0), (0,0)], # 1번 상하좌우
        [(-1,0), (1,0), (0,0), (0,0)], # 2번 상 하
        [(0,0), (0,0), (0,-1), (0,1)], # 3번 좌 우
        [(-1,0), (0,0), (0,0), (0,1)], # 4번 상 우
        [(0,0), (1,0), (0,0), (0,1)],  # 5번 하 우
        [(0,0), (1,0), (0,-1), (0,0)], # 6번 하 좌
        [(-1,0), (0,0), (0,1), (0,0)]  # 7번 상 좌
    ]
    # directions = [[1,0],[0,1],[-1,0],[0,-1]]
    #
    # for i in range(4):
    #     direc = directions[i]
    #     nr = r+direc[0]
    #     nc = c+direc[1]
    hour = 0# 시작하자 마자 1시간을 쓰니깐( 그자리에서)
    # visited
    visited = [[0]* M for _ in range(N)] # 방문 체크를 위해
    stack = [[[0,0 ],[]]]
    count = 0
    # 이제 구현을 하려면  #arr는 있고, 시작 위치 R, C 에서 각각 어디로 갈 수 있는 지 확인하기
    while hour < L: #종료조건 시간을 다 쓴 경우
        start = arr[R][C] # 시작 위치
        stack.append(start)
        visited[R][C] = 1 # 시작하자 마자 방문 하니깐
        hour += 1
        # 그다음 갈 수 있는지 확인
        # 건너갈 수 있는 범위 arr 이내 그리고 0 이 아닐때
        for d in range(4):# 4방향 확인
            nr = R + d_list[start][d][0]
            nc = C + d_list[start][d][1]
            # 갈 수 있는 지 확인
            # 그리고 만날 수 있는 지 확인

            if 0<= nr< N and 0 <= nc < N and arr[nr][nc] !=0 and visited[nr][nc]!= 1: # 배열 이내이면서 방문하지 않았고, 0이 아닐 경우
                next_box = arr[nr][nc]
                # 만약 상 방향에서 만났다면
                if (d ==0 and  d_list[next_box][1][0] + d_list[start][d][0] ==0 and d_list[next_box][1][1] + d_list[start][d][1] == 0):
                    # :# 상방향으로 가는 중 만난거니깐 아래와 위 비교
                    visited[nr][nc] = 1  # 그쪽 지점으로 가기
                    R, C = nr, nc

                # 만약 하 방향에서 만났다면
                if (d == 1 and d_list[next_box][0][0] + d_list[start][d][0] == 0 and d_list[next_box][0][1] +d_list[start][d][1] == 0):
                    visited[nr][nc] = 1  # 그쪽 지점으로 가기
                    R, C = nr, nc
                # 만약 좌 방향에서 만났다면
                if (d ==2 and  d_list[next_box][3][0] + d_list[start][d][0] ==0 and d_list[next_box][3][1] + d_list[start][d][1] == 0):
                    visited[nr][nc] = 1  # 그쪽 지점으로 가기
                    R, C = nr, nc
                # 만약 우 방향에서 만낫다면
                if (d ==3 and  d_list[next_box][2][0] + d_list[start][d][0] ==0 and d_list[next_box][2][1] + d_list[start][d][1] == 0):
                    visited[nr][nc] = 1  # 그쪽 지점으로 가기
                    R, C = nr, nc
                # if d_list[next_box][d][0] + d_list[start][d][0] ==0 and d_list[next_box][d][1] + d_list[start][d][1] == 0: #연결되어ㅆ는 경우

        # 만약 갈 수 있는 부분이 없는 경우라면

    for r in range(N):
        for c in range(M):
            if visited[r][c] == 1:  #방문한 경우
                count+=1
    return count



T = int(input()) # 테스트 케이스
for tc in range(1, T+1):
    N, M, R, C, L = map(int,input().split()) # N, M 칸 , R,C 맨홀 위치 L 시간
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = solve(R, C, L)
    print(f'#{tc} {result}')