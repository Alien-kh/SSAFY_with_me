T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우 방향 벡터
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_cnt = 0

    # 모든 좌표에 대해 탐색
    for r in range(N):
        for c in range(N):
            cnt = 1
            cr, cc = r, c
            
            # 이동 가능한 값이 있는지 확인 (플래그 변수 없이 구현)
            for d in range(4):
                nr = cr + dr[d]
                nc = cc + dc[d]
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] < arr[cr][cc]:
                    break
            else:
                continue
            
            # 더 이상 작은 값이 없을 때까지 반복
            while True:
                min_value = arr[cr][cc]
                next_r, next_c = -1, -1
                
                # 4방향 탐색
                for d in range(4):
                    nr = cr + dr[d]
                    nc = cc + dc[d]
                    
                    # 범위 확인 및 더 작은 값 찾기
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] < min_value:
                        min_value = arr[nr][nc]
                        next_r, next_c = nr, nc
                
                # 더 작은 값이 없으면 종료
                if next_r == -1 and next_c == -1:
                    break
                
                # 더 작은 값으로 이동 및 카운트 증가
                cr, cc = next_r, next_c
                cnt += 1
            
            # 최대 이동 횟수 갱신
            max_cnt = max(max_cnt, cnt)

    print(f"#{tc} {max_cnt}")

# 이 코드에서는 플래그 변수를 사용하지 않고, else 문을 활용하여 이동 가능한 값이 없는 경우 바로 다음 반복으로 넘어갑니다.
# 이동 가능하면 끝까지 이동하며, 이동 횟수의 최댓값을 구합니다.