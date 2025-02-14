#어디에단어가들어갈수있을까
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    word_blank_cnt = 0  # 단어가 들어갈 수 있는 칸의 개수

    # 가로 방향 검사
    for i in range(N):
        cnt = 0  # 연속된 1의 개수
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1  # 1이면 연속된 개수 증가
            else:
                if cnt == K:  # 연속된 칸이 K이면 카운트
                    word_blank_cnt += 1
                cnt = 0  # 끊기면 초기화
        if cnt == K:  # 행이 끝났을 때 K만큼 채워졌다면 추가
            word_blank_cnt += 1

    # 세로 방향 검사
    for j in range(N):
        cnt = 0  # 연속된 1의 개수
        for i in range(N):
            if puzzle[i][j] == 1:
                cnt += 1  # 1이면 연속된 개수 증가
            else:
                if cnt == K:  # 연속된 칸이 K이면 카운트
                    word_blank_cnt += 1
                cnt = 0  # 끊기면 초기화
        if cnt == K:  # 열이 끝났을 때 K만큼 채워졌다면 추가
            word_blank_cnt += 1

    print(f'#{tc} {word_blank_cnt}')
