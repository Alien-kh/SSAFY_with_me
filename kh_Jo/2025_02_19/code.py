from collections import deque
T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = list(map(int, input().split())) # 8개의 숫자를 입력 받기
    my_queue = deque() # 덱 만들어주기
    for num in arr: # 덱 안에 숫자들 넣어주기
        my_queue.append(num)
    last_num = True # 마지막 번호가 0이 될 때 까지
    while last_num:
        for i in range(1, 6): # 1사이클은 1~5까지
            a = my_queue.popleft() # 맨 앞 숫자 빼주기
            if (a -i) > 0 : # 빼주면서 뒤로 보낼때 0이 아니라면 계속 진행
                my_queue.append(a-i)
            else: # 만약에 0이라면 종료
                my_queue.append(0)
                last_num = False
                break # for 문 탈출

    print(f'#{tc}',*my_queue)