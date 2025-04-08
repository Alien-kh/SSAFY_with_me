T = int(input())  # 테스트케이스
for tc in range(1, T + 1):
    N = int(input())  # 전선의 갯수
    wires = []  # 기존 선들을 저장
    dot = 0     # 교차점 갯수
    for i in range(N):
        A, B = map(int, input().split())    # A 전봇대에 걸려있는 위치, B 전봇대에 걸려있는 위치
        for prev_A, prev_B in wires:
            if A < prev_A and B > prev_B:
                dot += 1
            elif A > prev_A and B < prev_B:
                dot += 1
        # 목록에 전선 추가
        wires.append((A,B))

    print(f'#{tc} {dot}')