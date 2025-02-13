# 조건이 겉보기에는 감도 안 잡힐 수 있지만,
# '하나를 끄면 뒤에께 전부 꺼진다' = '앞에서부터 같은 열의 조작후 리스트와 다른 값인 현재상태 리스트 값이 있을 경우 거기서부터 바꾼다'
# 라는 발상으로 접근하면 괜찮아 보였다.

def switch_on(before_line, after_lane):
    search_line = before_line
    global switch_num
    for _ in range(len(before_line)):
        for idx in range(len(before_line)):
            if before_line[idx] != after_lane[idx]:
                switch_num += 1
                for on_off_idx in range(idx, len(before_line)):
                    if search_line[on_off_idx] == 1:
                        search_line[on_off_idx] = 0
                    else:
                        search_line[on_off_idx] = 1


testcase = int(input())

for tc_idx in range(1, testcase + 1):
    switch_line = int(input())
    before_line = list(map(int, input().split()))
    after_lane = list(map(int, input().split()))
    switch_num = 0

    switch_on(before_line, after_lane)

    print(f'#{tc_idx} {switch_num} ')
