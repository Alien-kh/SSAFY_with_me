# 10451. 순열 사이클 개수 구하기
# 이 문제는 오히려 그림을 그려야만 함. (1 2 3 4 5 6 7 8)
#                                 (3 2 7 8 1 4 5 6)
# 입력 데이터를 받으면 바로 순열의 사이클이 만들어지고, 언젠가 자기 자신으로 돌아오는 형태가 됨.
# visited 라는 방문 체크 리스트를 만든 다음에 순열 사이클을 찾을 때 마다 방문한 노드는 1이 된다.
# visited의 1 ~ N번까지 다 1이 되었을 때, 반복은 종료되고 cnt가 곧 순열 사이클의 개수가 된다. 

def permutation(N, data):
    visited = [0] * (N + 1)     # 방문 체크
    cnt = 0

    # 모든 노드를 탐색.
    for i in range(1, N+1):
        if not visited[i]:  # 방문하지 않았다면
            cnt += 1
            current = i     # 현재 내가 가야하는곳.

            # DFS 탐색. 주어지는 데이터에 갈 수 있는 곳은 다 가야하니까.
            while visited[current] != 1:    # 재 방문하면 while문이 끝남.
                visited[current] = 1    # 방문 처리
                current = data[current - 1]

    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    result = permutation(N, data)
    print(result)