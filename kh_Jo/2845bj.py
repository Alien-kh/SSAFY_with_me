L, P = map(int, input().split()) # L = 넓이 P = 사람
lst = list(map(int, input().split())) # 각 뉴스 숫자
total = L * P # 사람 수
result = [] # 결과를 넣을 리스트
for num in lst: # 각 뉴스마다 실제값이랑 비교
    result.append(num-total)
print(*result) # 결과 unpacking