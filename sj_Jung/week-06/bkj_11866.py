from collections import deque

people_len, delete_num = map(int, input().split()) # 전체 인원수, 삭제시킬 단위 숫자

josephus_que = deque() # 큐 선언

answer = [] # 빈 정답 리스트

for i in range(1, people_len + 1):
    josephus_que.append(str(i)) # 요세푸스 맵 제작

index = delete_num - 1 # 인덱스는 -1해야 정답.

while josephus_que: # 큐가 전부 없어질때 까지 반복
    for _ in range(index):
        josephus_que.append(josephus_que.popleft()) # pop 시킬 지점까지 원형 큐 형태 사용.
    answer.append(josephus_que.popleft()) # 삭제시킬 지점이 오면 answer로 pop시키기.

answer = ', '.join(answer) # 출력 형식을 맞추기 위한 언패킹

print(f'<{answer}>')