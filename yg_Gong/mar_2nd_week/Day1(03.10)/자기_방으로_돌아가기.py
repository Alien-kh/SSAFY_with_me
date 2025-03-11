T = int(input())  # 테스트케이스

for tc in range(1, T + 1):
    N = int(input())  # 돌아가야할 학생 수
    corridor = [0] * 200    # 복도
    for i in range(N):
        current, move = map(int, input().split())  # current : 현재 위치, move: 이동해야할 방 위치



