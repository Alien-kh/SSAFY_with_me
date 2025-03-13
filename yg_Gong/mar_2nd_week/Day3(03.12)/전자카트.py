def cart(idx, total_cost):
    global min_cost

    # 모든 관리구역을 방문한 경우
    if idx == N - 1:
        total_cost += battery[path[idx]][1]  # 1번으로 돌아옴
        min_cost = min(min_cost, total_cost)  # 최소 배터리 소모량 여부
        return

    for i in range(2, N + 1):
        if not visited[i]:  # 방문하지 않은 곳만 선택
            visited[i] = True
            path[idx] = i
            cart(idx + 1, total_cost + battery[path[idx - 1]][i])
            visited[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    battery = [[0] * (N + 1)]
    for i in range(1, N + 1):
        battery[i] = [0] + list(map(int, input().split()))


    min_cost = 0xffffffff  # 최소 배터리 사용량
    visited = [False] * (N + 1)  # 방문 체크
    path = [0] * (N - 1)  # 관리구역 순서

    path[0] = 1  # 항상 1번에서 출발
    visited[1] = True  # 1번은 방문했다고 체크
    cart(1, 0)  # 사무실 다음 위치부터 시작

    print(f'#{tc} {min_cost}')
