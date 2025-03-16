# 스위치조작

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0  # 스위치 조작 횟수

    for i in range(N):
        if A[i] != B[i]:  # 현재 전등 상태가 목표 상태와 다르면
            cnt += 1  # 스위치 눌러야 함
            # i번부터 N번까지 반전
            for j in range(i, N):
                A[j] = 1 - A[j]  # 0 → 1, 1 → 0 변경

    print(f'#{tc} {cnt}')
