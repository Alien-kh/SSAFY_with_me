# 1333 백준
# 이 문제의 후기. 조건의 이해가 매우 매우 중요한 문제. 특히 시작과 끝 구간을 포함하냐 않하냐에 따라
# 맞고 틀리고가 결정되는 아주 무서운 문제.

N, L, D = map(int,input().split()) # N곡의 락, L초의 길이, D초에 한번씩 울림.

end_rock = (N-1) * (L + 5) + L  # 락 전체 재생 시간.

t = 0   # 전화벨이 울리는 시간 변수
while True:
    # 락이 모두 끝났다면 전화벨 소리가 들림.
    if t >= end_rock:
        print(t)
        break

    music_rock = False 
    # 전화벨을 들을 수 있는 시간이 락의 재생 구간에 있는지 확인해야 한다.
    for i in range(N):
        start = i * (L + 5)
        end = start + L

        # 전화벨이 락의 시작과 정확히 일치하면 못 듣는다!
        if t == start:     
            music_rock = True
            break

        if start< t < end:   # 락 재생 도중에 전화가 온 경우
            music_rock = True
            break

    if not music_rock:
        print(t)
        break

    # 전화벨을 듣지 못한 시간대라면 다음 시간대로 가야한다.
    t += D