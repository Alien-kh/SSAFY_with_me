T = int(input())  # 테스트 케이스 수

for _ in range(T):
    N, M = map(int, input().split())  # N: 문서의 개수, M: M번째 문서의 인덱스
    my_queue = list(map(int, input().split()))  # 각 문서의 중요도

    # 문서의 중요도를 인덱스와 함께 튜플로 저장 (중요도, 원래 인덱스)
    queue = [(my_queue[i], i) for i in range(N)]

    cnt = 0
    while queue:
        # 가장 중요한 문서가 앞에 오는지 확인
        max_priority = queue[0][0]
        for doc in queue:
            if doc[0] > max_priority:
                max_priority = doc[0]

        if queue[0][0] == max_priority:
            cnt += 1
            # M번째 문서가 출력된다면 종료
            if queue[0][1] == M:
                print(cnt)
                break
            # 출력된 문서 제거
            queue.pop(0)
        else:
            # 가장 중요한 문서가 아니면 맨 뒤로 보내기
            queue.append(queue.pop(0))