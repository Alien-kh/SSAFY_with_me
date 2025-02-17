# 파리퇴치3 풀이

def solve(N, M, arr):
    max_flies = 0

    # 스프레이 범위 (+, x)
    delta_plus = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상, 하, 좌, 우 + 모양 이동
    delta_x = [[-1, -1], [-1, 1], [1, -1], [1, 1]]  # 11시, 1시, 7시 5시의 X모양 이동

    for i in range(N):
        for j in range(N):
            for delta in [delta_plus, delta_x]:
                flies = arr[i][j]   # 기준 지점도 더하기.
                for xy in delta:
                    for d in range(1, M):
                        ni, nj = i + xy[0] * d, j + xy[1] * d
                        if 0 <= ni < N and 0 <= nj < N:  # N x N 배열을 넘어가는 경우를 막기위한 조건.
                            flies += arr[ni][nj]  # + 방향 /  x 방향 의 파리의 합.

                # 최대 파리 값 찾기
                if flies > max_flies:
                    max_flies = flies

    return max_flies


T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = solve(N, M, arr)
    print(f"#{test} {result}")