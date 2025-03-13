T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())
    # 시작점이 도착점보다 큰 경우 미리 자리 바꿔놓기
    data = [list(sorted(map(int, input().split()))) for _ in range(N)]
    data.sort()  # 구간 정렬  # 오류의 주범

    boxs = []  # 빈 상자를 준비
    for start, end in data:
        start -= (start + 1) % 2  # 시작점: 짝수면 1을 빼서 홀수로 만든다
        end += end % 2  # 끝점: 홀수면 1을 더해 짝수로 만든다

        # 구간을 배치할 상자 찾기
        for box in boxs:  # 상자 속에 data를 하나씩 담기  # box: 리스트 속 리스트
            if all(y < start or end < x for x, y in box):  # 상자 속 모든 구간과 겹치지 않는다면
                box.append((start, end))  # 담기 (주의: 튜플로 묶어야 line 15에서 언패킹이 됨)
                break
        else:  # 담을 수 있는 상자가 없다면
            boxs.append([(start, end)])  # 새로운 box []에 (start, end) 담기

    print(f'#{tc} {len(boxs)}')