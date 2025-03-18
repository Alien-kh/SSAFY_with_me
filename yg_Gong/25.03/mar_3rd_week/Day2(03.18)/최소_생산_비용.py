# 순열으로 모든 경우의수를 구하고, 그 중 최소값 찾기
# 중복값 없어야됨!!(중복순열x)
# 모든 공장을 방문하고 최소 비용을 찾는 함수
def factory_cost(x, sum_cost):
    global min_cost
    # 애초에 sum_cost가 현재 최소값보다 커지면
    # 함수를 더 진행시킬 필요가 없음
    if sum_cost > min_cost: # 시간 초과나서 추가한 코드
        return
    # x =  공장 idx
    if x == N:  # 3공장 다 들리면 함수종료
        if sum_cost < min_cost:  # break 전에 현재 sum_cost가 최소값인지 확인
            min_cost = sum_cost
        return


    for i in range(N):  # 제품 idx
        if visited[i] == 0 :
            visited[i] = 1
            factory_cost(x + 1, sum_cost + factory[x][i])
            visited[i] = 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]

    min_cost = 0xffffffff
    visited = [0] * N
    factory_cost(0,0)
    print(f'#{tc} {min_cost}')