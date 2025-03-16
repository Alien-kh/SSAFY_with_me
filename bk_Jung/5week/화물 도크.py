T = int(input())
for tc in range(1,T+1):
    N = int(input())
    truck = []
    for i in range(N):
        a,b = map(int,input().split())
        truck.append((a,b))

    truck.sort(key = lambda x:x[1])
    cnt = 0
    end_time = 0
    for i,j in truck:

        if i >= end_time:
            cnt += 1
            end_time = j

    print(f'#{tc} {cnt}')