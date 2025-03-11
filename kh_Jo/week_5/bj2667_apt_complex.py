from collections import deque


def solve():
    visited = [[0] * N for _ in range(N)]
    direction = [[-1,0], [1,0], [0, -1], [0, 1]]
    dq = deque()
    c_cnt = 1 # 단지수를 나타내는
    result = [] # 단지를 담을 list
    for r in range(N):
        for c in range(N):
            h_count = 0 # 집 개수 세기 용
            is_complex = False # 단지 인지 확인
            if arr[r][c] == '1' and visited[r][c] == 0: #방문한 적이 없고, 아파트가 있다면
                dq.append([r,c])
                visited[r][c] = 1
                h_count += 1
                while dq:
                    curr_r, curr_c = dq.popleft()
                    for d in direction:
                        nr, nc = curr_r + d[0], curr_c + d[1]
                        if 0 <= nr < N and 0 <= nc < N: # 지도 안에 있고
                            if arr[nr][nc] == '1' and visited[nr][nc] ==0: # 다음 갈 곳이 방문한 적이 없고, 갈 수 있을 때
                                dq.append([nr,nc])
                                visited[nr][nc]= c_cnt
                                h_count += 1
            if h_count >=1: # 한 집이라도 있으면
                is_complex = True

            if is_complex:
                result.append(h_count)
                c_cnt += 1
    result = sorted(result)
    return c_cnt-1, result


N = int(input()) # 아파트 지도의 크기
arr = [input() for _ in range(N)] # N * N 배열
complex_count, f_result = solve()
print(complex_count)
print(*f_result, sep='\n')
