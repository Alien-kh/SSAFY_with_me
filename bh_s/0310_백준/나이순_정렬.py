N = int(input())
lst = []
for _ in range(N):
    data = input().split()
    lst.append(data)

# sort()를 사용하여 나이 기준으로 정렬
lst.sort(key=lambda x: int(x[0]))

# 정렬된 결과 출력
for i in range(N):
    print(*lst[i])