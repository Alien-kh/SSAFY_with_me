from collections import deque
import sys

member_num = int(sys.stdin.readline()) # 전체 줄 서있는 사람 수

# 대기 줄 리스트, 대기줄에서는 맨 앞사람이 나가야하므로, deque를 활용해보기로 하였음.
mem_list = deque(map(int, sys.stdin.readline().split()))

enter_num = 1 # 다음에 들어갈 사람을 알려주는 index 번호

waiting_num = -1 # 대기 zone index 번호(top 역할)
waiting_list = [] # 대기 zone 구역 리스트

escape_code = 0 # 반복문 탈출용

while True:
    if waiting_list:  # waiting zone에 사람이 있다면
        escape_code += 1 # 여기 if문 지나감
        if waiting_list[waiting_num] == enter_num:  # 만약 제일 뒤에 있는 사람이 입장 번호랑 같다면...
            waiting_list.pop()  # 빼고 입장시키기
            waiting_num -= 1  # 대기 top -1
            enter_num += 1  # 다음 번호 호출
            escape_code = 0
            continue

    if mem_list: # 본래 줄에 사람이 있다면
        escape_code += 1 # 여기 if문 지나감
        if mem_list[0] == enter_num: # 줄에 맨 앞에 서있는 번호가 들어가야할 번호랑 같다면...
            mem_list.popleft() # mem_list에서 제거하고, entered_list에 추가
            enter_num += 1 # 다음 번호 호출
            escape_code = 0
            continue

        elif mem_list[0] != enter_num: # 줄에 맨 앞에 서있는 번호가 들어가야할 번호랑 다르다면
            waiting_list.append(mem_list.popleft())  # 아닐 시 waiting_list 추가
            waiting_num += 1  # 대기 top +1
            escape_code = 0
            continue

    if not mem_list and not waiting_list : # 전부 제대로 받았다면
        break

    if escape_code == member_num: # 전부 제대로 받을 수 없는 상태라면
        break

if enter_num - 1 == member_num: # 만약 전부 제대로 받았다면
    print('Nice')
else: # 만약 전부 제대로 받을 수 없는 상태라면, 만약 mem_list에 없는데도 waiting_list 만 있는 경우를 고려한 코드
    print('Sad')