def solve(start):
    global cnt
    visited[start] = 1 # 현재 방문한 돌다리를 1로 바꾼다.
    if start + jump_len[start] < len(jump_len) and visited[start + jump_len[start]] != 1: # 오른쪽 돌로 가게 만드는 if문
        cnt += 1 # 방문 돌 갯수 추가
        solve(start + jump_len[start]) # 재귀로 다음 방문할 돌 찾기
    if start - jump_len[start] > -1 and visited[start - jump_len[start]] != 1: # 왼쪽 돌로 가게 만드는 if문
        cnt += 1 # 방문 돌 갯수 추가
        solve(start - jump_len[start]) # 재귀로 다음 방문할 돌 찾기
    return # 더 이상 갈 수 있는 돌이 없거나 방문할 돌이 없다면 return


stone_bridge = int(input()) # 돌다리 갯수
jump_len = list(map(int, input().split())) # 돌다리당 표시된 점프 거리
start = int(input()) - 1 # 시작지점. 인덱스로 쓰일거라 -1 처리

cnt = 1 # 방문한 돌 갯수. 무조건 시작점인 첫번째 돌다리는 건넌다.

visited = [0] * stone_bridge # 방문한 돌다리 확인용

solve(start) # def 호출

print(cnt)