N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

# 회의를 끝나는 시간 기준으로 정렬
data.sort(key=lambda x: (x[1],x[0]))

select = []
prev_end = 0  # 첫 회의는 이전 회의 종료 시간이 없으므로 0부터 시작

for meeting in data:
    start, end = meeting
    # 회의 시작 시간이 이전 회의 종료 시간보다 같거나 크면 선택
    if start >= prev_end:
        select.append(meeting)
        prev_end = end  # 선택된 회의의 종료 시간으로 업데이트

print(len(select))