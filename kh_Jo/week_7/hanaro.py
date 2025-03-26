import heapq
def prim():
    q = [(0, 0)] # cost, node
    MST = [0] * N
    # MST[0] = 1 # 시작 지점 체크 =>안에서 체크해주니깐 무필요
    min_cost = 0 # 최소 비용 체크
    dists = [float('inf')] * N # 최소비용 저장 리스트
    dists[0] = 0 # 시작 최소비용은 언제나 0
    while q:
        # COST가 가장 낮은 후보부터 나옴
        cost, node = heapq.heappop(q)

        if MST[node]: # 만약 방문했다면
            continue
        # node 로 가는 간선을 확정짓는 코드
        MST[node] = 1
        min_cost += cost


        for next_node in range(N):
            if MST[next_node]:
                continue
            new_cost = ((X_list[node]- X_list[next_node])**2 + (Y_list[node] - Y_list[next_node])**2) * tax

            if new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(q,(new_cost, next_node))
    return round(min_cost)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X_list = list(map(int, input().split()))
    Y_list = list(map(int, input().split()))
    tax = float(input())
    result = prim()
    print(f'#{tc} {result}')