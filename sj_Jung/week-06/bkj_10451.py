import sys

def dfs(start):
    global cnt
    visited[start] = 1 # 도착한 곳에 1 추가.
    if visited[indexed_list[start]] == 1: # 만약 순환순열이 끝났다면 cnt를 1 추가하고 멈춘다.
        cnt += 1
        return
    else:
        dfs(indexed_list[start]) # 재귀하여 순열을 완성환다.


testcase = int(sys.stdin.readline())

for tc_idx in range(1, testcase + 1):
    num_len = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    indexed_list = [x - 1 for x in num_list] # num_list에서 입력받은 값들을 전부 index 값에 맞게 변환시켜준다.
    visited = [0] * num_len # DFS를 위한 visited 정의

    cnt = 0  # 순환하는 순열의 갯수를 저장하는 변수.  즉, 이 문제의 답.

    for i in range(len(indexed_list)):
        if visited[i] == 0: # 1이면 그 변수는 시작지점이 아니므로 패스
            dfs(i) # dfs def 호출

    print(cnt)
