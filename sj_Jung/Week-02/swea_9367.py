test_case = int(input())
for tc_index in range(1,test_case+1):
    carrot_len = int(input()) # 당근 갯수 입력
    carrot_list = list(map(int,input().split())) # 당근 리스트 입력

    before_carrot = carrot_list[0] # 비교군이 될 0번 당근 값 먼저 저장
    max_counting = 1 # 최대 연속 증가값 저장
    counting = 1 # 연속 증가값 저장

    for c_idx in range(1, carrot_len): # 0번 당근은 비교군으로 빼뒀으니 1번부터 확인
        if max_counting < counting:  # 현 최대값과 비교하여 값이 더 크면
            max_counting = counting  # 갱신한다.
        if carrot_list[c_idx] > before_carrot: # 만약 커진다면
            counting += 1 # 카운팅한다.
        else: # 연속하지 않는다면
            counting = 1 # 그리고 초기화한다.
        before_carrot = carrot_list[c_idx] # 비교군을 교체한다.

    if max_counting < counting:  # 종료전 마지막 갱신, 현 최대값과 비교하여 값이 더 크면
        max_counting = counting  # 갱신한다.
    print(f'#{tc_index} {max_counting}')