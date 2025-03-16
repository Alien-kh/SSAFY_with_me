# 무게, 적재용량 내림차순 정렬
# 무게 가장 큰 컨테이너를 적재용량 가장 큰 트럭에 적재
# 만약 컨테이너가 가장 큰 트럭에 안들어가면 그 다음 무거운거랑 비교
T = int(input())

for tc in range(1, T + 1):
    N,M = map(int, input().split()) # N:컨테이너 수, M: 트럭수
    container_weight = list(map(int, input().split()))
    truck_weight = list(map(int, input().split()))
    # 무게, 적재용량 내림차순 정렬
    container_weight.sort(reverse=True)
    truck_weight.sort(reverse=True)

    weight = 0  # 적재컨테이너 무게
    for i in range(len(truck_weight)):
        for j in range(len(container_weight)):
            if container_weight[j] <= truck_weight[i]:
                weight += container_weight[j]
                container_weight.pop(j)
                break

    print(f'#{tc} {weight}')

