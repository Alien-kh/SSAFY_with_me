def dfs(battery, cnt, idx, curr):
    global min_cnt#  최소 카운트 전역변수 설정
    if min_cnt < cnt: # 최솟값보다 더 높다면 의미 X
        return
    if curr+battery >= N: # 만약 현재 지점 + 남은 배터리수가 도착지점보다 높다면 갈 수 있음
        if min_cnt >= cnt: # min_cnt 갱신
            min_cnt = cnt
        return
    if idx == len(arr) -1: # 여기까지 오면 더 갈 수 없음
        return

    # 만약 여유배터리가 있따면 넘어갈 수 있음
    if battery > 1:
        dfs(battery-1,  cnt, idx+1, curr+1) # 배터리만 줄이고 앞으로 나아가기
    dfs(arr[idx+1], cnt+1, idx+1, curr+1) # 배터리를 교체한 경우
'''
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1

'''


T = int(input())
for tc in range(1, T+1):
    arr =list(map(int,input().split()))
    N = arr[0]
    min_cnt = 21e8
    dfs(arr[1], 0,  1, 1)
    print(f'#{tc} {min_cnt}')
