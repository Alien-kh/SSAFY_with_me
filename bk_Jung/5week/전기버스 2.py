def charge(idx,now_battery,cnt): # idx -> 정류장
    global min_cnt

    if cnt >= min_cnt:
        return

    if idx == N: # 최종 목적지라면 리턴
        if cnt < min_cnt:
            min_cnt = cnt
        return
    if now_battery > 0 and idx < N:
        # 교환 안한 경우
        charge(idx+1,now_battery-1,cnt)

    if now_battery >= 0 and idx < N: # 거리가 목적지보다 작을때만
        # 교환 한 경우
        charge(idx+1,arr[idx]-1,cnt+1)




T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    N = arr[0]

    min_cnt = 1e9
    charge(1,arr[1],0)
    print(f'#{tc} {min_cnt}')