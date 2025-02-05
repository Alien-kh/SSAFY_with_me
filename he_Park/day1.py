# 백준 2480

from collections import Counter

A, B, C = map(int, input().split())
lst = [A, B, C]
number_count = dict(Counter(lst))  # {주사위 숫자:나온 개수}
reverse = {v:k for k, v in number_count.items()}  # {나온 개수:주사위 숫자}

if 3 in reverse:  # 3개가 다 같다면
    print(10000 + A * 1000)

elif 2 not in reverse:  # 3개 다 다르다면
    print(max(lst) * 100)
    
else:  # 2개만 같다면
    print(1000 + reverse[2] * 100)