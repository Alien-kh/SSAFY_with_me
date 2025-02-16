def solve(arr, N, M):
    dr = [-1, 1, 0, 0] # 상 하 좌 우
    dc = [0, 0, -1, 1]
    max_sum_v = arr[0][0] # 일단 대충 지정
    for r in range(N): # 행
        for c in range(M): # 열
            sum_v = arr[r][c] # 상 하 좌 우 + 자기 자신을 위해 sum 설정(미리 넣어 두기)
            for d in range(4): # 4 방향으로 더할 곳 지정
                nr = r+ dr[d]
                nc = c+ dc[d]
                if 0 <= nr < N and 0 <= nc < M: # 만약 arr에 값들이 다 있다면
                    sum_v += arr[nr][nc] # 각 항들 더하기
            if max_sum_v < sum_v: # 더한 후 최댓값 비교
                max_sum_v = sum_v
    return max_sum_v


T = int(input())
for tc in range(1, T+1):
    N, M =map(int,input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    print(f'#{tc} {solve(arr, N, M)}')