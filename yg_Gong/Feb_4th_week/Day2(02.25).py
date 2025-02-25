# 부재중 전화
# N: 노래곡수 L:노래길이, D:전화벨 간격
N, L, D = map(int, input().split())

time = 0
ring = 0  # 전화벨이 울리는 시간

while True:
    # 노래 구간 체크
    song_playing = False
    for i in range(N):
        start = i * (L + 5)  # 노래 시작 시간
        end = start + L - 1  # 노래 끝나는 시간 (노래 시작이 0초부터라 -1)
        if start <= ring <= end:  # 노래 중이면 패스
            song_playing = True
            break

    if not song_playing:  # 노래가 안 나오면 정답 출력
        print(ring)
        break

    ring += D  # 전화벨 울리는 시간 증가

