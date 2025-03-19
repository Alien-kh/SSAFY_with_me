from collections import deque

testcase = int(input())

for tc_idx in range(1, testcase + 1):
    total_page, target_page = map(int, input().split()) # 총 페이지 수와 목표 페이지 수를 받음
    print_list = deque(map(int, input().split())) # 프린트 대기 내역을 queue로 받음
    print_cnt = 0 # 지금까지 출력한 양을 기록할 변수

    while True: # 목표치에 닿을때까지 무한 반복
        if print_list[0] < max(print_list): # 만약 우선순위가 더 높은게 있다면
            print_list.append(print_list.popleft()) # 뒷 순서로 미룬다.
            if target_page == 0: # 만약 지금 페이지가 목표 페이지 였다면
                target_page += len(print_list) - 1 # 밀려난 만큼 인덱스도 재지정한다.
            else: # 아니라면
                target_page -= 1 # 앞으로 순서가 당겨졌을테니 1씩 감소시킨다.
        else: # 만약 우선순위가 더 높은게 없다면(즉, 출력해야한다면)
            if target_page == 0: # 만약 목표 페이지라면
                print_list.popleft() # 출력하고
                print_cnt += 1 # 프린트 수에 1 추가 후
                break # 반복문을 종료시킨다.
            print_list.popleft() # 아니라면, 출력하고
            target_page -= 1 # 순서가 당겨졌으니 1 마이너스 하고
            print_cnt += 1 # 프린트 수에 1 추가한다.

    print(print_cnt)
