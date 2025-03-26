def solve():
    my_v = 1
    while True:
        # 각 주기의 범위에 맞게 확인
        if (my_v - 1) % 15 + 1 == E and (my_v - 1) % 28 + 1 == S and (my_v - 1) % 19 + 1 == M:
            return my_v
        my_v += 1

E, S, M = map(int, input().split())
print(solve())
