# 딕셔너리 이용.

N, M = map(int, input().split())

lst = [0] * N
str_to_idx = {}  # 문자열 → 인덱스를 빠르게 찾기 위한 딕셔너리

for i in range(N):
    lst[i] = input()
    str_to_idx[lst[i]] = i + 1  # 1-based index 저장

for _ in range(M):
    check = input()

    if check.isdigit():  # 숫자인 경우
        print(lst[int(check) - 1])
    else:  # 문자열인 경우
        print(str_to_idx[check])
