
def solve(M, N):
    lst = []

    for i in range(M, N+1):
        if find_num(i):
            lst.append(i)

    if len(lst) == 0:
        return -1, -1

    sum_v = 0
    for j in range(len(lst)):
        sum_v += lst[j]

    return sum_v, lst[0]


def find_num(num):
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False


M = int(input())
N = int(input())

a, b = solve(M, N)
if a == -1 and b == -1:
    print(-1)
else:
    print(a)
    print(b)
