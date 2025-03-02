N = int(input().strip())
arr = [list(map(int,input().split())) for _ in range(N)]
# 시너지 점수를 먼저 구해놓기
syn_list = [[0] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        syn_list[r][c] = arr[r][c] + arr[c][r] # 1,3,3,1 시너지

visited = [False]* N # 선택한 사람 빼기
visited[0] = True # 일단 첫 번째 사람 start팀에 때려 넣기
min_diff = 21e8 # 일단 엄청 큰 수
def compute_diff(): # 팀 정수 능력 합산
    start_t = []
    link_t = []
    for i in range(N):
        if visited[i]:
            start_t.append(i)
        else:
            link_t.append(i)
    sum_start = 0 # start팀 합산
    for i in range(len(start_t)):
        for j in range(i+1, len(start_t)):
            sum_start += syn_list[start_t[i]][start_t[j]]

    sum_link = 0 # start팀 합산
    for i in range(len(link_t)):
        for j in range(i+1, len(link_t)):
            sum_link += syn_list[link_t[i]][link_t[j]]
    return abs(sum_start - sum_link)

def dfs(idx, start_count):
    global min_diff
    if idx == N: # 모든 사람 배정했을 떄
        if start_count == N // 2: # (0번이 스타트팀이니깐 절반일 떄 조건 만족(반반)
            diff = compute_diff()
            if diff < min_diff:
                min_diff = diff
            if min_diff ==0:
                return
        return

    remain = N - idx # 남은 사람 수
    link_count = idx - start_count # 링크팀 사람 수는 결국 idx(팀에 들어간 사람 숫자 - 스타트팀 숫자)
    if start_count < N//2:
        visited[idx] = True # start팀에 들어가면 true
        dfs(idx+1, start_count+1)
        visited[idx] = False # 다음에 사용하 수 있게 초기화
    if link_count < N //2:
        visited[idx] = False
        dfs(idx+1, start_count) # link팀은 false인 사람들이 들어가는 거니깐
dfs(1, 1)
print(min_diff)