# 끝나는 시간을 기준으로 오름차순 정렬
# 빠르게 끝나는 회의를 선택
# 해당 회의 종료 이후로 가능한 회의중, 종료시간 빠른 회의 선택(반복)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    box = []
    for i in range(N):
        time = list(map(int, input().split()))
        box.append(time)
    box.sort(key=lambda x: x[1])  # 종료시간 기준으로 오름차순 정렬

    end_time = 0  # 종료시간 저장할 변수
    cnt = 0  # 화물 갯수

    for i in box:
        if i[0] >= end_time:  # 시작시간이 전화물의 종료시간과 같거나 크다면
            cnt += 1  # cnt +1
            end_time = i[1]  # 종료시간을 방금 선택한 화물의 종료시간으로 변경

    print(f'#{tc} {cnt}')
