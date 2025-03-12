# in 연산으로 꺼내서 비교하려 한다면 set으로 접근하면 엄청 빠르다.

N = int(input())
card = set(map(int, input().split()))
M = int(input())
compare_c = list(map(int, input().split()))
new_lst = [0] * M
for i in range(M):
    if compare_c[i] in card:
        new_lst[i] = 1

print(*new_lst)
