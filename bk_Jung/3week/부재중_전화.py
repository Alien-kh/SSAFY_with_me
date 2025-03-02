N, L, D = map(int, input().split())

time = 0  # 전화벨이 울리는 시간
music_end = (N - 1) * (L + 5) + L  # 마지막 곡이 끝나는 시간

while time < music_end:
    start = 0
    for i in range(N):
        start = i * (L + 5)
        end = start + L
        if start <= time < end:  # 전화벨이 음악 중간에 울리면 다음 울리는 시간으로 넘어감
            break
    else:
        # 모든 음악을 체크했는데도 전화벨이 음악 중이 아닐 때 울리면 출력
        print(time)
        exit()
    
    time += D  # 다음 전화벨 울리는 시간

# 만약 전화벨이 모든 음악 중에만 울렸다면, 음악이 끝난 후 처음으로 울리는 시간 출력
print(time)
