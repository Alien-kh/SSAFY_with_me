album_include, song_len, phone_bell = map(int, input().split()) # 정보 입력

ans = 0 # 답 추출용
do_not_disturb = [] # 노래 지속 시간과 노래 빈 시간 시각화

for i in range(album_include): # 지도 제작
    for j in range(song_len):
        do_not_disturb.append(1) # 노래 들리는 부분

    if i == album_include-1: # 노래가 끝나는 부분에는 멈추도록
        break
    else: # 노래와 노래 사이
        for _ in range(5):
            do_not_disturb.append(0) # 노래 안 들리는 부분

ringringring = 0 # 전화 울리는 구간을 설정

while True:
    if ringringring >= len(do_not_disturb): # 노래가 끝났다면
        ans = ringringring # 노래 끝나고 받음
        break
    elif do_not_disturb[ringringring] == 0: # 전화를 받을 수 있다면
        ans = ringringring # 답으로 설정.
        break
    else: # 받을 수 없다면
        ringringring += phone_bell # 다음 벨 울리는 지점으로 이동

print(ans)