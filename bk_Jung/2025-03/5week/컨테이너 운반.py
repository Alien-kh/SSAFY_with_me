T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    container = list(map(int,input().split()))
    truck = list(map(int,input().split()))

    container.sort(reverse= True)
    truck.sort(reverse=True)

    result = 0
    for i in range(M):
        for j in range(len(container)):
            if truck[i] >= container[j]:
                result += container[j]
                container.pop(j)
                break

    if len(container) == N:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {result}')
